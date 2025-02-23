int actuador = 12;

void setup() {
  pinMode(actuador, OUTPUT);
}

void loop() {
  digitalWrite(actuador, 1);
  delay(1000);
  digitalWrite(actuador, 0);
  delay(1000);
}
