# ViBraille 
A Project By Nupur Divekar, Aarsh Mehta and Krish Agarwal
## Project Description
This project aims to create an accessible tool for converting printed text into Braille. Utilizing a combination of OCR (Optical Character Recognition) and a custom-built Braille sensation machine, this project offers a unique solution for visually impaired individuals to read printed material. The system uses a camera to capture images of text, processes the text via OCR, converts it into Braille representation, and then actuates solenoids in a Braille display to render the text tactilely.

## Features
- **Optical Character Recognition**: Converts text from images into digital text using Tesseract OCR.
- **Braille Conversion**: Translates digital text into Braille representation.
- **Real-Time Text-to-Braille Conversion**: Processes images in real-time and displays the corresponding Braille.
- **Customizable Braille Display**: Utilizes solenoids for a tactile Braille display, allowing users to feel the Braille representation of the text.
- **Arduino-Powered Control**: Manages the solenoid actuation using an Arduino, ensuring precise control for accurate Braille representation.

## Hardware Requirements
- Arduino Uno/Mega
- Solenoids for Braille display
- Circuit components (transistors, diodes, resistors)
- Camera or a device for capturing images of text
- Power supply for solenoids
- Connecting wires and breadboard

## Software Requirements
- Python 3.x
- PySerial for Arduino communication
- Tesseract OCR
- PIL (Python Imaging Library) for image processing
- Watchdog for file system monitoring

## Usage
1. **Setup Hardware**: Assemble the Braille display with solenoids connected to the Arduino. Ensure all hardware connections are secure.
2. **Install Software Dependencies**: Install Python, Tesseract OCR, PySerial, PIL, and Watchdog libraries.
3. **Run the Python Script**: Execute the script to start the OCR and Braille conversion process. The script monitors a designated folder for new images.
4. **Image Processing**: Place images of the text in the monitored folder. The script processes these images, extracts the text, and converts it to Braille.
5. **Braille Display**: The Arduino receives the Braille code and actuates the solenoids to display the text in Braille.
6. **Interact with the Braille Display**: Users can read the tactile Braille output corresponding to the printed text.
