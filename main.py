import pytesseract
from PIL import Image

# Function to extract text from an image
def extract_text(image_path):
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"Error: {e}"

# Replace 'image.jpg' with the path to your image file
text = extract_text('/Users/aarshmehta/Downloads/istockphoto-1227331821-612x612.jpg')
print(text)
