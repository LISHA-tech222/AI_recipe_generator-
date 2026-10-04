# 🍳 AI-Driven Recipe Generator

An intelligent AI-powered recipe generator that creates personalized recipes based on user inputs such as ingredients, dietary preferences, allergies, and language. The system also supports OCR-based ingredient extraction and multilingual recipe generation.

---

## 🚀 Features

- 🧠 AI-based recipe generation using a local LLM (Ollama - LLaMA 3.2 3B)
- 📷 OCR-based ingredient extraction from images (Tesseract)
- ⚠️ Allergy-aware ingredient filtering and substitution (gluten, dairy, seafood, nuts)
- 🥗 Diet preferences: Vegetarian, Non-Vegetarian, Vegan
- 🍝 Cuisines: Indian, Italian, Chinese, Arabian, Korean
- 🌍 Multilingual recipe generation (English, Hindi, Tamil, Telugu)
- 👥 Adjustable servings and maximum cooking time
- 📄 PDF export (English only)

---

## 🛠️ Tech Stack

- Python
- Gradio (UI)
- Ollama (LLM - LLaMA 3.2 3B)
- Tesseract OCR (pytesseract)
- Pillow
- FPDF (PDF generation)

---

## 📁 Project Structure

```
AI_Recipe_Generator/
├── app.py            # Gradio UI and main generation pipeline
├── functions.py      # OCR, allergy processing, LLM call, PDF export
├── requirements.txt  # Python dependencies
└── readme.md
```

---

## 📦 Requirements

Make sure you have the following installed:

### 1️⃣ Python
- Python 3.9 or above  
👉 Download: https://www.python.org/downloads/

---

### 2️⃣ Ollama (for LLM)

👉 Download: https://ollama.com/download

After installing, run:

```bash
ollama pull llama3.2:3b
````

---

### 3️⃣ Tesseract OCR

👉 Download (Windows):
[https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)

During installation:
✔ Check **"Add to PATH"**

---

### 4️⃣ Python Libraries

Install all dependencies:

```bash
pip install -r requirements.txt
```

If requirements.txt is missing, install the core packages manually:

```bash
pip install gradio pytesseract pillow opencv-python fpdf ollama
```

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <your-repo-link>
cd AI_Recipe_Generator
```

---

### Step 2: Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Run Ollama

Make sure Ollama is running in background.

Test that the model is available:

```bash
ollama list
```

You should see `llama3.2:3b` in the list.

---

### Step 5: Run the Application

```bash
python app.py
```

You will see:

```
Running on http://127.0.0.1:7860
```

Open it in your browser.

---

## 📸 How to Use

1. Enter ingredients manually OR upload an image
2. Select:

   * Diet preference
   * Cuisine
   * Allergies (one of: `gluten`, `dairy`, `seafood`, `nuts`)
   * Output language
   * Servings and cooking time (minutes)
3. Click **Generate Recipe**
4. View the recipe
5. Download PDF (English only)

If both an image and text are provided, the OCR output and typed ingredients are combined.

---

## ⚠️ Notes

* OCR works best with **printed, high-contrast images**
* Handwritten input may produce noisy results
* PDF export supports **English only**
* Multilingual output is generated directly by the LLM
* Allergy substitution uses a built-in database covering gluten, dairy, seafood and nuts; the LLM is also instructed to avoid the allergen
* Ollama must be running locally before generating a recipe
* The PDF is saved as `Generated_Recipe.pdf` in the project folder

---

## 🧪 Example Inputs

* Ingredients: `tomato, rice, chicken`
* Allergy: `dairy`
* Language: `Hindi`

---

## 📌 Future Improvements

* Advanced OCR for handwritten text
* Unicode PDF support
* Voice input integration
* Nutritional analysis

---

## 👩‍💻 Author

Lisha Choudhary
B.E CSE (Data Science)

---

## 📄 License

This project is for academic and research purposes.