import PyPDF2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def extract_text_from_image(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)