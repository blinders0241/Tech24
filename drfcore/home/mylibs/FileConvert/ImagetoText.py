import pytesseract
from PIL import Image
# Set the tesseract path in the script
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_from_image(image_path):
    # Open the image file
    img = Image.open(image_path)
    
    # Use pytesseract to do OCR on the image
    text = pytesseract.image_to_string(img)
    
    return text

# Usage
filePath = r"C:\SIMPLY_Official\2024\TechHome241\drfcore\home\mylibs\FileConvert\\"
text = ocr_from_image(filePath + 'page5.jpg')
print(text)