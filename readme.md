# 🍳 AI-Driven Recipe Generator

An intelligent AI-powered recipe generator that creates personalized recipes based on user inputs such as ingredients, dietary preferences, allergies, and language. The system also supports OCR-based ingredient extraction and multilingual recipe generation.

---

## 🚀 Features

- 🧠 AI-based recipe generation using LLM (Ollama - LLaMA 3.2)
- 📷 OCR-based ingredient extraction from images
- ⚠️ Allergy-aware ingredient filtering and substitution
- 🌍 Multilingual recipe generation (English, Hindi, Tamil, Telugu)
- 📄 PDF export (English only)
- 🎯 Personalized cooking instructions

---

## 🛠️ Tech Stack

- Python
- Gradio (UI)
- Ollama (LLM - LLaMA 3.2)
- Tesseract OCR
- OpenCV / PIL
- FPDF (PDF generation)

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

If requirements.txt is missing, install manually:

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

Test:

```bash
ollama list
```

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
   * Allergies
   * Language
3. Click **Generate Recipe**
4. View recipe
5. Download PDF (English only)

---

## ⚠️ Notes

* OCR works best with **printed, high-contrast images**
* Handwritten input may produce noisy results
* PDF export supports **English only**
* Multilingual output is generated directly by the LLM

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