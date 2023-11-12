import os
import time
import serial
import pytesseract
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Serial port configuration
ser = serial.Serial('COM_PORT', 9600)  # Update COM port as needed

# Braille conversion dictionary
braille_dict = {
    # Your alphabet to braille mapping here
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
