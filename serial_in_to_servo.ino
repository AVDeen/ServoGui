#include <Servo.h>

Servo myservo;

int val;
String inputString = "";
boolean stringComplete = false;

// Initial setup
// Serial communication at 9600 baud
// Servo motor at pin 9
void setup() {
  Serial.begin(9600);
  myservo.attach(9);
  inputString.reserve(200);
}

// Process loop
void loop() {
  if (stringComplete) {
    val = inputString.toInt();
    Serial.print("I recieved: ");
    Serial.println(val, DEC);

    if (val >= 0 && val <= 180) {
      myservo.write(val);
      delay(15);
    } else {
      Serial.println("Invalid value");
    }
    inputString = "";
    stringComplete = false;
  }
}

// Handle incoming serial 
// PySerial will send a series of integers from 0 to 180 indicating the next location of the servo, followed by a \n character
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (isDigit(inChar)) {
      inputString += inChar;
    }
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}

