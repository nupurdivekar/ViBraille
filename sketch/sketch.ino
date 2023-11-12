const int solenoidPins[6] = {2, 3, 4, 5, 6, 7}; // Define the pins for the solenoids

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 6; i++) {
    pinMode(solenoidPins[i], OUTPUT); // Initialize solenoid pins as outputs
  }
}

void loop() {
  if (Serial.available() > 0) {
    String brailleCode = Serial.readStringUntil('\n');
    
    for (int i = 0; i < brailleCode.length(); i += 6) {
      String character = brailleCode.substring(i, i + 6);
      actuateBrailleCharacter(character);
      delay(200); // Delay between characters
    }
  }
}

void actuateBrailleCharacter(String brailleCharacter) {
  // Reset all solenoids to LOW
  for (int i = 0; i < 6; i++) {
    digitalWrite(solenoidPins[i], LOW); 

  }

  // Hardcoded actions for each Braille character
  if (brailleCharacter == "100000") { // Braille for 'a'
    digitalWrite(solenoidPins[0], HIGH);
  } else if (brailleCharacter == "110100") { // Braille for 'b'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
  } else if (brailleCharacter == "110000") { // Braille for 'c'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
  } else if (brailleCharacter == "110100") { // Braille for 'd'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
  } else if (brailleCharacter == "100100") { // Braille for 'e'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
  } else if (brailleCharacter == "111000") { // Braille for 'f'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
  } else if (brailleCharacter == "111100") { // Braille for 'g'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
  } else if (brailleCharacter == "101100") { // Braille for 'h'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
  } else if (brailleCharacter == "011000") { // Braille for 'i'
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
  } else if (brailleCharacter == "011100") { // Braille for 'j'
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
  } else if (brailleCharacter == "100010") { // Braille for 'k'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "101010") { // Braille for 'l'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "110010") { // Braille for 'm'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "110110") { // Braille for 'n'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "100110") { // Braille for 'o'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "111010") { // Braille for 'p'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "111110") { // Braille for 'q'
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
    digitalWrite(solenoidPins[5], HIGH);
  } else if (brailleCharacter == "101110") { // Braille for 'r'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "011010") { // Braille for 's'
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "011110") { // Braille for 't'
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "100011") { // Braille for 'u'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
    digitalWrite(solenoidPins[5], HIGH);
  } else if (brailleCharacter == "101011") { // Braille for 'v'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
    digitalWrite(solenoidPins[5], HIGH);
  } else if (brailleCharacter == "011101") { // Braille for 'w'
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[2], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
  } else if (brailleCharacter == "110011") { // Braille for 'x'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
    digitalWrite(solenoidPins[5], HIGH);
  } else if (brailleCharacter == "110111") { // Braille for 'y'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[1], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
    digitalWrite(solenoidPins[5], HIGH);
  } else if (brailleCharacter == "100111") { // Braille for 'z'
    digitalWrite(solenoidPins[0], HIGH);
    digitalWrite(solenoidPins[3], HIGH);
    digitalWrite(solenoidPins[4], HIGH);
    digitalWrite(solenoidPins[5], HIGH);
  } else if (brailleCharacter == "000000") { // Braille for space
    delay(200);
  }
}