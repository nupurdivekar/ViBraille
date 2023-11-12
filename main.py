import os
import time
import serial
import pytesseract
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract.exe'

# Serial port configuration
ser = serial.Serial('COM_PORT', 9600)  # Update COM port as needed

# Braille conversion dictionary
braille_dict = {
    'a': '100000', 'b': '101000', 'c': '110000', 'd': '110100',
    'e': '100100', 'f': '111000', 'g': '111100', 'h': '101100',
    'i': '011000', 'j': '011100', 'k': '100010', 'l': '101010',
    'm': '110010', 'n': '110110', 'o': '100110', 'p': '111010',
    'q': '111110', 'r': '101110', 's': '011010', 't': '011110',
    'u': '100011', 'v': '101011', 'w': '011101', 'x': '110011',
    'y': '110111', 'z': '100111', 
    ' ': '000000',  # Space
    '1': '100000', '2': '101000', '3': '110000', '4': '110100', 
    '5': '100100', '6': '111000', '7': '111100', '8': '101100', 
    '9': '011100', '0': '011000',
    # Add more mappings for punctuation if needed
}

# Function to convert text to braille
def text_to_braille(text):
    return ''.join(braille_dict.get(char, '000000') for char in text.lower())

# Function to process image with OCR
def process_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    braille = text_to_braille(text)
    ser.write(braille.encode())  # Send braille to Arduino

# Class to handle file system events
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
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is created.
            process_image(event.src_path)

# Initialize and run the watcher
watcher = Watcher("/Users/aarshmehta/Desktop/ViBraille/images")
watcher.run()
