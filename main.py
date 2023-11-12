import os
import time
import serial
import pytesseract
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from picamera import PiCamera

# Initialize camera
camera = PiCamera()

# Directory to store images
image_dir = "pi/ViBraille/images"  
os.makedirs(image_dir, exist_ok=True)

# Function to capture an image
def capture_image(image_name):
    image_path = os.path.join(image_dir, image_name)
    camera.start_preview()
    time.sleep(2)  # Camera warm-up time
    camera.capture(image_path)
    camera.stop_preview()
    return image_path

# OCR and Braille Conversion Setup
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Update this path

braille_dict = {
    'a': '100000', 'b': ' ', 'c': '110000', 'd': '110100',
    'e': '100100', 'f': '111000', 'g': '111100', 'h': '101100',
    'i': '011000', 'j': '011100', 'k': '100010', 'l': '101010',
    'm': '110010', 'n': '110110', 'o': '100110', 'p': '111010',
    'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011',
    'y': '110111', 'z': '100111', ' ': '000000'
    # Add more mappings for numbers and punctuation if needed.
}
# Serial Communication Setup
arduino_serial = serial.Serial(port='/dev/tty.usbmodem1101', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for connection to establish

def text_to_braille(text):
    braille_string = ""
    for char in text.lower():  # Convert the entire text to lowercase
        braille_string += braille_dict.get(char, '000000')  # Default to '000000' for unknown characters
    return braille_string

def process_image(image_path):
    print("Processing image:", image_path)
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted text:", text)
    braille = text_to_braille(text)
    print("Braille representation:", braille)

    # Send each 6-bit Braille character separately
    for i in range(0, len(braille), 6):
        braille_char = braille[i:i+6]
        print(braille[i:i+6])
        arduino_serial.write(braille_char.encode())
        time.sleep(0.2)  # Short delay between characters; adjust as needed


class Watcher:
    def __init__(self, directory_to_watch):
        self.observer = Observer()
        self.directory_to_watch = directory_to_watch

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.directory_to_watch, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.bmp', '.gif')):
            print(f"New image file detected: {event.src_path}")
            process_image(event.src_path)

# Initialize and run the watcher
watcher = Watcher("/Users/aarshmehta/Desktop/ViBraille/images")
try:
    watcher.run()
except Exception as e:
    print(f"An error occurred: {e}")
