from picamera import PiCamerafrom PIL import Image
import pytesseract

# Path to the Tesseract executable
# Only needed if Tesseract is not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image using PIL
image = Image.open('path_to_image.jpg')

# Use Tesseract to do OCR on the image
text = pytesseract.image_to_string(image, lang='eng')

print(text)   

