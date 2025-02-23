int sensor = A0;
int actuador = 6;

void setup() {
  pinMode(actuador, OUTPUT);
}

int v;
void loop() {
  v = analogRead(sensor);
  v = v / 4;
  analogWrite(actuador, v);
  delay(100);
}