int potentiometers[4] = {A0, A1, A2, A3};
int values[4];
String c;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void loop() {
  for(int i = 0; i < 4; i++)
  {
    values[i] = analogRead(potentiometers[i]);
    delayMicroseconds(1000);
  }
  c = "I-" + String(values[0]) + "-" + String(values[1]) + "-" + String(values[2]) + "-" + String(values[3]) + "-F";
  Serial.println(c);
  delay(10);
}
