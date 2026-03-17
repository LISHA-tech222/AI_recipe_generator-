import gradio as gr
import time

from functions import (
    get_recipe,
    process_allergy,
    extract_ingredients_from_image,
    export_recipe_pdf
)

# ----------------------------
# MAIN PIPELINE FUNCTION
# ----------------------------

def generate_recipe_pipeline(img, txt, diet, cuisine, allergy, lang, serv, time_limit):

    start_time = time.time()

    # ---------------- OCR + TEXT MERGE ----------------
    image_text = ""

    if img:
        try:
            image_text = extract_ingredients_from_image(img)
            if image_text is None:
                image_text = ""
        except Exception as e:
            print("OCR ERROR:", e)
            image_text = ""

    ingredients = (str(image_text) + " " + (txt or "")).strip()

    print("OCR OUTPUT:", image_text)
    print("FINAL INGREDIENTS:", ingredients)

    if not ingredients or ingredients.lower() in ["", "none"]:
        return "⚠ Please provide ingredients (text or image).", None

    # ---------------- ALLERGY PROCESSING ----------------
    safe_ingredients = process_allergy(ingredients, allergy)

    print("SAFE INGREDIENTS:", safe_ingredients)

    # ---------------- RECIPE GENERATION ----------------
    recipe = get_recipe(
        safe_ingredients,
        diet,
        cuisine,
        serv,
        time_limit,
        lang,
        allergy
    )

    # ---------------- PDF EXPORT ----------------
    if recipe and lang == "English":
        recipe_text, pdf_file = export_recipe_pdf(recipe)
    else:
        recipe_text = recipe if recipe else "⚠ Recipe generation failed."
        pdf_file = None

    end_time = time.time()
    response_time = end_time - start_time

    print(f"[INFO] Recipe generated in {response_time:.2f} seconds")

    return recipe_text, pdf_file


# ----------------------------
# GRADIO UI
# ----------------------------

with gr.Blocks() as demo:
    gr.Markdown("# AI-Driven Recipe Generator")
    gr.Markdown("### Smart, Allergy-Safe & Multilingual Cooking Assistant")

    with gr.Row():
        with gr.Column():
            gr.Markdown("### User Inputs")

            groceries = gr.Textbox(
                label="Available Ingredients",
                placeholder="tomatoes, rice, chicken"
            )

            ingredient_image = gr.Image(
                label="Upload Ingredient Image (OCR)",
                type="filepath"
            )

            recipe_type = gr.Radio(
                ["Vegetarian", "Non-Vegetarian", "Vegan"],
                label="Diet Preference"
            )

            cuisine_style = gr.Dropdown(
                ["Indian", "Italian", "Chinese", "Arabian", "Korean"],
                label="Cuisine"
            )

            allergies = gr.Textbox(
                label="Food Allergies",
                placeholder="nuts, dairy, gluten"
            )

            language = gr.Dropdown(
                ["English", "Hindi", "Tamil", "Telugu"],
                label="Output Language"
            )

            servings = gr.Number(
                label="Servings",
                value=1,
                precision=0
            )

            max_time = gr.Number(
                label="Cooking Time (mins)",
                value=30,
                precision=0
            )

            generate_btn = gr.Button("Generate Recipe")

        with gr.Column():
            recipe_output = gr.Textbox(
                label="Generated Recipe",
                lines=18,
                interactive=False
            )

            download_pdf = gr.File(label="Download Recipe PDF")

    generate_btn.click(
        fn=generate_recipe_pipeline,
        inputs=[
            ingredient_image,
            groceries,
            recipe_type,
            cuisine_style,
            allergies,
            language,
            servings,
            max_time
        ],
        outputs=[recipe_output, download_pdf]
    )

demo.launch()