int pinPWM = 6;

void setup() {
  pinMode(pinPWM, OUTPUT);
}

void loop() {
  for(int i = 0; i < 255; i++) {
  analogWrite(pinPWM, i);
  delayMicroseconds(10);
  }
  delay(100);
  for (int i = 255; i > 0; i--) {
  analogWrite(pinPWM, i);
  delayMicroseconds(10);
  }
  delay(10);
}
