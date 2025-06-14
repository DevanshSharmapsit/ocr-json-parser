from flask import Flask, request, jsonify, render_template
import pytesseract
from PIL import Image

app = Flask(__name__)

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image)

    return jsonify({
        "extracted_text": text.strip()
    })

if __name__ == '__main__':
    app.run(debug=True)
