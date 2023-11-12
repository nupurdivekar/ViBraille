import os
import time
import serial
import pytesseract
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# OCR and Braille Conversion Setup
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Update this path

braille_dict = {
    'a': '100000', 'b': '101000', 'c': '110000', 'd': '110100',
    'e': '100100', 'f': '111000', 'g': '111100', 'h': '101100',
    'i': '011000', 'j': '011100', 'k': '100010', 'l': '101010',
    'm': '110010', 'n': '110110', 'o': '100110', 'p': '111010',
    'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011',
    'y': '110111', 'z': '100111',
    # Add more mappings for numbers and punctuation if needed.
}

# Serial Communication Setup
arduino_serial = serial.Serial(port='/dev/tty.usbmodem1101', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for connection to establish

def text_to_braille(text):
    return ''.join(braille_dict.get(char, '000000') for char in text.lower())

def process_image(image_path):
    print("Processing image:", image_path)  # Print the image path being processed
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted text:", text)  # Print the extracted text
    braille = text_to_braille(text)
    print("Braille representation:", braille)  # Print the Braille representation
    arduino_serial.write(braille.encode())  # Send Braille to Arduino


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
    def on_any_event(event):
        print(f"Event detected: {event}")  # This line will print any event detected
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            process_image(event.src_path)


# # Initialize and run the watcher
watcher = Watcher("/Users/aarshmehta/Desktop/ViBraille/images")
watcher.run()
try:
    watcher = Watcher("/Users/aarshmehta/Desktop/ViBraille/images")
    watcher.run()
except Exception as e:
    print(f"An error occurred: {e}")

def process_image(image_path):
    print("Processing image:", image_path)  # Print the image path being processed
    text = pytesseract.image_to_string(Image.open(image_path))
    print("Extracted text:", text)  # Print the extracted text
    braille = text_to_braille(text)
    print("Braille representation:", braille)  # Print the Braille representation
    arduino_serial.write(braille.encode())  # Send Braille to Arduino
#process_image("/Users/aarshmehta/Desktop/ViBraille/images/istockphoto-1227331821-612x612.jpg")  # Update with a test image path