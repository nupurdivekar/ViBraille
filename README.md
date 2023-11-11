# ViBraille

A portable Braille reader that translates text into Braille characters, which are then represented physically using solenoids for tactile feedback. The system uses a camera to capture images of text, which are processed using Optical Character Recognition (OCR) software to convert the visual text into digital text. This text is then translated into Braille, and an array of solenoids, controlled by an Arduino microcontroller, is actuated to represent the Braille characters. The solenoids create raised dots that can be felt by a user, mimicking the Braille reading experience. The device aims to provide a compact, efficient, and accessible way for visually impaired individuals to read printed text in real-time. Additionally, an ultrasonic sensor is incorporated to ensure the text is at an optimal distance for image capture, enhancing the system's usability.

**Overview of the System Workflow:**

Image Capture: The camera takes a picture of the text.

OCR Processing: The image is processed by OCR software to extract the text.

Text to Braille Translation: The text is converted into Braille code.

Data Transfer: The Braille code is sent to the Arduino.

Vibration Output: The Arduino controls the motors to create Braille patterns.

Important Considerations:

Accuracy of OCR: The effectiveness of the system depends greatly on the accuracy of the OCR process. Good lighting and clear text are important.

Efficient Communication: The method of transferring data from the OCR system to the Arduino should be reliable and fast.

Intuitive Motor Layout: The arrangement of the vibration motors should be intuitive for the user, mimicking the layout of Braille characters.

This process combines hardware interaction, software processing, and tactile feedback to convert visual text into a format that can be 'read' through touch by Braille-literate users.
