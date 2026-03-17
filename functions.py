import cv2
import ollama
import pytesseract
from PIL import Image
from fpdf import FPDF

#from googletrans import Translator
# -------------------------------
# ALLERGEN KNOWLEDGE BASE
# -------------------------------

ALLERGEN_DB = {
    "gluten": {
        "remove": ["wheat", "wheat flour", "barley", "rye"],
        "substitute": {
            "wheat flour": "rice flour",
            "wheat": "millet flour"
        }
    },
    "dairy": {
        "remove": ["milk", "butter", "cheese", "ghee", "cream"],
        "substitute": {
            "milk": "almond milk",
            "butter": "olive oil",
            "cheese": "vegan cheese"
        }
    },
    "seafood": {
        "remove": ["shrimp", "fish", "crab", "lobster", "prawn"],
        "substitute": {
            "shrimp": "tofu",
            "fish": "mushroom"
        }
    },
    "nuts": {
        "remove": [
            "peanut", "peanut butter",
            "almond", "cashew", "walnut",
            "pistachio", "hazelnut"
        ],
        "substitute": {
            "peanut butter": "sunflower seed butter",
            "peanut": "sunflower seeds",
            "almond": "pumpkin seeds",
            "cashew": "soy chunks"
        }
    }
}
# -------------------------------
# 1. OCR INGREDIENT EXTRACTION
# -------------------------------
def extract_ingredients_from_image(image_path):
    try:
        if not image_path:
            return ""

        print("IMAGE PATH:", image_path)

        img = Image.open(image_path)

        text = pytesseract.image_to_string(img)

        print("RAW OCR TEXT:", text)

        return text.lower().strip()

    except Exception as e:
        print("OCR ERROR:", e)
        return ""


# -------------------------------
# 2. HYBRID ALLERGY PROCESSING
# -------------------------------

def process_allergy(ingredients, allergy):
    """
    Removes or substitutes allergenic ingredients
    using structured ALLERGEN_DB
    """

    if not allergy:
        return ingredients

    ingredients = ingredients.lower()
    allergy = allergy.lower()

    if allergy in ALLERGEN_DB:
        remove_items = ALLERGEN_DB[allergy]["remove"]
        substitutes = ALLERGEN_DB[allergy]["substitute"]

        for item in remove_items:
            if item in ingredients:
                if item in substitutes:
                    ingredients = ingredients.replace(item, substitutes[item])
                else:
                    ingredients = ingredients.replace(item, "")

    return ingredients



# -------------------------------
# 4. AI RECIPE GENERATION (LLM LOGIC)
# -------------------------------
def get_recipe(ingredients, diet, cuisine, servings, time, language, allergy):
    """
    Generates recipe using Ollama LLM
    """

    prompt = f"""
    You are a professional chef.

    Create a detailed {cuisine} {diet} recipe using these ingredients:
    {ingredients}

    Important:
    - Strictly avoid all ingredients related to {allergy}.
    - If any allergenic ingredient appears, replace it with a safe alternative.
    - Ensure quantities are realistic.
    - Servings: {servings}
    - Cooking time within {time} minutes.
    - Provide clear step-by-step instructions.
    Language Instructions:
    - If language is English, write in standard English.
    - If language is Hindi, write in proper Devanagari script (हिंदी लिपि). Do NOT use Roman Hindi.
    - If language is Tamil, write in proper Tamil script (தமிழ் எழுத்து). Do NOT use Roman Tamil.
    - If language is Telugu, write in proper Telugu script (తెలుగు లిపి). Do NOT use Roman Telugu.
    Generate the recipe in {language}.
    """

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]



# -------------------------------
# 5. MULTILINGUAL TRANSLATION
# -------------------------------
def translate_recipe(recipe_text, language):
    """
    Translation disabled for demo stability.
    Returns English recipe.
    """
    return recipe_text


# -------------------------------
# 6. PDF EXPORT
# -------------------------------
def export_recipe_pdf(recipe_text):
    """
    Exports generated recipe as a PDF file
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in recipe_text.split("\n"):
        pdf.multi_cell(0, 8, line)

    file_path = "Generated_Recipe.pdf"
    pdf.output(file_path)

    return recipe_text, file_path
