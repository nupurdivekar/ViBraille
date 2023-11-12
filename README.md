# ViBraille 
## A Project By Nupur Divekar, Aarsh Mehta, and Krish Agarwal

## Project Description
This project aims to create an accessible tool for converting printed text into Braille. Utilizing a combination of OCR (Optical Character Recognition) and a custom-built Braille sensation machine, this project offers a unique solution for visually impaired individuals to read printed material. The system uses a Raspberry Pi camera to capture images of text, processes the text via OCR on the Raspberry Pi, converts it into Braille representation, and then actuates solenoids in a Braille display to render the text tactilely.

## Features
- **Optical Character Recognition**: Converts text from images into digital text using Tesseract OCR.
- **Braille Conversion**: Translates digital text into Braille representation.
- **Real-Time Text-to-Braille Conversion**: Processes images in real-time and displays the corresponding Braille.
- **Customizable Braille Display**: Utilizes solenoids for a tactile Braille display, allowing users to feel the Braille representation of the text.
- **Arduino-Powered Control**: Manages the solenoid actuation using an Arduino, ensuring precise control for accurate Braille representation.
- **Raspberry Pi for Image Capturing**: Uses a Raspberry Pi 2 with a camera module to capture images of the text.

## Hardware Requirements
- Raspberry Pi 2 with Camera Module
- Arduino Uno
- 6 Solenoids for Braille display
- Circuit components (transistors, diodes, resistors)
- Power supply for solenoids and Raspberry Pi
- Connecting wires and breadboard

## Software Requirements
- Python 3.x
- PySerial for Arduino communication
- Tesseract OCR
- PIL (Python Imaging Library) for image processing on Raspberry Pi
- Watchdog for file system monitoring on Raspberry Pi

## Usage
1. **Setup Hardware**: Connect the Raspberry Pi Camera Module to the Raspberry Pi and assemble the Braille display with solenoids connected to the Arduino. Ensure all hardware connections are secure.
2. **Install Software Dependencies**: On the Raspberry Pi, install Python, Tesseract OCR, PySerial, PIL, and Watchdog libraries.
3. **Run the Python Script on Raspberry Pi**: Execute the script on the Raspberry Pi to start the OCR process. The script captures images using the Raspberry Pi camera, processes these images, extracts the text, and converts it to Braille.
4. **Image Processing and Braille Conversion**: The Raspberry Pi 2(along with its camera module) captures, processes images in real-time, extracts text, and converts it into Braille representation in binary.
5. **Braille Display Activation**: The Braille code is sent from the Raspberry Pi to the Arduino, which actuates the solenoids to display the text in Braille.
6. **Interact with the Braille Display**: Users can read the tactile Braille output, which corresponds to the printed text.
