# 📄 Document Intelligence & Image Analyzer

An AI-powered application that extracts text from documents and images, summarizes content, answers questions, and converts text into speech. Built using **Streamlit**, **Google Gemini**, **OCR**, and **PDF processing**.

---

## 🚀 Features

- 📂 Upload PDF documents
- 🖼️ Upload image files (JPG, JPEG, PNG)
- 🔍 Extract text using OCR
- 📑 Extract text from PDF documents
- 🤖 AI-generated text summarization
- 💬 Ask questions about the uploaded document
- 🔊 Convert extracted or summarized text into speech
- 🎨 Simple and interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- LangChain
- PyMuPDF (fitz)
- Pillow (PIL)
- pytesseract
- gTTS
- python-dotenv

---

## 📁 Project Structure

```
Document-Intelligence-Image-Analyzer/
│
├── app.py
├── requirements.txt
├── .env
│
├── utils/
│   ├── llm.py
│   ├── ocr.py
│   ├── pdf_utils.py
│   └── tts.py
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Document-Intelligence-Image-Analyzer.git
```

### 2. Navigate to the project

```bash
cd Document-Intelligence-Image-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a PDF or image.
2. The application extracts text.
3. AI summarizes the extracted content.
4. Ask questions related to the document.
5. Listen to the extracted or summarized text using Text-to-Speech.

---

## 📦 Required Libraries

```
streamlit
Pillow
PyMuPDF
pytesseract
gTTS
langchain
langchain-google-genai
python-dotenv
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Applications

- Document summarization
- Image text extraction
- Academic document analysis
- Business document processing
- Report analysis
- Invoice and receipt text extraction
- AI-powered document question answering
- Text-to-Speech accessibility

---

## 🔮 Future Enhancements

- Support for DOCX and TXT files
- Multi-language OCR
- Voice input for questions
- Chat history
- Download summarized content
- Multiple document support
- PDF highlighting
- Cloud deployment

---


## ⭐ If you like this project

Give this repository a ⭐ on GitHub and share it with others!
