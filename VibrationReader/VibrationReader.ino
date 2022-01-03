int analogPin = A0;

int val = 0;

void setup() {
  Serial.begin(9600);
  //Serial.print(1);

}

void loop() {
  val = analogRead(analogPin);
  Serial.print(val);
  delay(50);
  }
