const int redLedPin = 9;    // Pin for Red LED
const int greenLedPin = 10; // Pin for Green LED
const int buzzerPin = 11;   // Pin for Buzzer

void setup() {
    pinMode(redLedPin, OUTPUT);
    pinMode(greenLedPin, OUTPUT);
    pinMode(buzzerPin, OUTPUT);
    Serial.begin(9600); // Start serial communication
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read(); // Read the command from serial
        if (command == '1') { // No mask detected
            digitalWrite(redLedPin, HIGH); // Turn on Red LED
            digitalWrite(greenLedPin, LOW); // Turn off Green LED
            digitalWrite(buzzerPin, HIGH); // Turn on Buzzer
        } else if (command == '0') { // Mask detected
            digitalWrite(redLedPin, LOW); // Turn off Red LED
            digitalWrite(greenLedPin, HIGH); // Turn on Green LED
            digitalWrite(buzzerPin, LOW); // Turn off Buzzer
        }
    }
}