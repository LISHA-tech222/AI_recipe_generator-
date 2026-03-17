# 🍳 AI-Driven Recipe Generator

An intelligent AI-powered recipe generator that creates personalized recipes based on user inputs such as ingredients, dietary preferences, allergies, and language. The system also supports OCR-based ingredient extraction and multilingual recipe generation.

---

## 🚀 Features

* **🧠 AI-based Generation:** Uses LLM (Ollama - LLaMA 3.2) for creative recipes.
* **📷 OCR Integration:** Extract ingredients directly from images of labels or lists.
* **⚠️ Allergy-Aware:** Automatic ingredient filtering and smart substitutions.
* **🌍 Multilingual:** Supports English, Hindi, Tamil, and Telugu.
* **📄 PDF Export:** Save your recipes for later (English only).
* **🎯 Personalization:** Tailors instructions to specific cuisines and preferences.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Interface:** Gradio
* **Intelligence:** Ollama (LLaMA 3.2:3b)
* **Vision:** Tesseract OCR, OpenCV, PIL
* **Document Engine:** FPDF

---

## 📦 Requirements

### 1. Python
* Python 3.9 or above 
* [Download Python](https://www.python.org/downloads/)

### 2. Ollama (Local LLM)
* [Download Ollama](https://ollama.com/download)
* After installation, pull the model:
    ```bash
    ollama pull llama3.2:3b
    ```

### 3. Tesseract OCR
* [Download for Windows](https://github.com/UB-Mannheim/tesseract/wiki)
* **Note:** Ensure you check **"Add Tesseract to your PATH"** during installation.

---

## ⚙️ Setup Instructions

### Step 1: Clone the Repository
```bash
git clone <your-repo-link>
cd AI_Recipe_Generator
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install gradio pytesseract pillow opencv-python fpdf ollama
```

### Step 4: Run the Application
1. Ensure Ollama is running (`ollama list` to verify).
2. Start the Python app:
   ```bash
   python app.py
   ```
3. Open the local URL provided: `http://127.0.0.1:7860`

---

## 📸 How to Use
1.  **Input:** Enter ingredients manually OR upload an image.
2.  **Filter:** Select Diet preference, Cuisine, Allergies, and Language.
3.  **Generate:** Click "Generate Recipe."
4.  **Save:** View the recipe and download the PDF (English only).

---

## ⚠️ Notes
* **OCR Quality:** Works best with printed, high-contrast images. Handwritten text may be less accurate.
* **PDF Support:** Currently supports English characters only due to font limitations.
* **Model:** Ensure your hardware can support running LLaMA 3.2 locally.

---

## 📌 Future Improvements
* Advanced OCR for handwritten text.
* Unicode/UTF-8 PDF support for multilingual exports.
* Voice-to-text input integration.
* Real-time nutritional analysis.

---

## 👩‍💻 Author
**Lisha Choudhary** *B.E CSE (Data Science)*

## 📄 License
This project is for academic and research purposes.
```
