/* 
 *  This file is used for testing and debugging the script on the PC, where I don't have
 *  GPIO pins. For this reason, this file isn't really well documentated nor is written 
 *  in an acceptable programming style.
 */

String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);

  for(int i = 2; i<=10; i++){
    analogWrite(i,255);
    digitalWrite(i,LOW);
  }
}

void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    if (inputString != "") {
      int pin = int(inputString[0]);
      int state = int(inputString[1]);
      pin -= 46;
      state -= 48;
      digitalWrite(pin, state);
      delay(10);
      /*
      Serial.print(pin);
      Serial.print(":");
      Serial.println(state);
      */
      Serial.print(inputString);
      inputString = "";
      stringComplete = false;
    }
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
