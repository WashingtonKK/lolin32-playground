int ledPIn = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(ledPIn, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hello Word! Jesus is on His way to take us home.");
  //digitalWrite(ledPIn, HIGH);
  //delay(500);
  digitalWrite(ledPIn, LOW);
  //delay(2000);
}
