# 🧠 OCR to JSON Parser

This is a simple Flask-based web app that allows users to upload an image (or scanned document) and extracts the text using OCR (Tesseract). The extracted content is returned in **JSON** format.

## 🔧 Tech Stack

- **Backend:** Python, Flask
- **OCR Engine:** Tesseract OCR via `pytesseract`
- **Image Processing:** Pillow
- **Frontend:** HTML + Tailwind CSS (CDN)
- **Output Format:** JSON

## 🌟 Features

- Upload image files (JPG, PNG, etc.)
- Extract text using OCR
- Return clean JSON response
- Minimal UI with Tailwind styling

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/DevanshSharmapsit/ocr-json-parser.git
cd ocr-json-parser
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Install Tesseract OCR
Windows:
Download from:
https://github.com/UB-Mannheim/tesseract/wiki

Update app.py:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
4. Run the Flask App
bash
Copy
Edit
python app.py
5. Access the App
Open your browser and go to:
http://localhost:5000

📸 Demo
Upload a file and receive output like:

json
Copy
Edit
{
  "extracted_text": "This is a test image with sample text."
}
🛠 Future Improvements
Support for PDF (via pdf2image)

Structured JSON output for invoices

Deploy to Render or Replit

📬 Contact
Created by Devansh Sharma

GitHub

LinkedIn

Portfolio

'''bash
