void setup() {
  pinMode(8,OUTPUT);
  pinMode(2,INPUT);
  pinMode(3,INPUT);
  pinMode(4,INPUT);
  pinMode(5,INPUT);
  pinMode(6,INPUT);
  Serial.begin(9600);
}

void loop() {
  if(digitalRead(2)==HIGH){
    Serial.write("B1");
    digitalWrite(8,HIGH);
    delay(1000);
    digitalWrite(8,LOW);
    delay(1000);
  }
  if(digitalRead(3)==HIGH){
    Serial.write("B2");
    digitalWrite(8,HIGH);
    delay(1000);
    digitalWrite(8,LOW);
    delay(1000);
  }
  if(digitalRead(4)==HIGH){
    Serial.write("B3");
    digitalWrite(8,HIGH);
    delay(1000);
    digitalWrite(8,LOW);
    delay(1000);
  }
  if(digitalRead(5)==HIGH){
    Serial.write("B4");
    digitalWrite(8,HIGH);
    delay(1000);
    digitalWrite(8,LOW);
    delay(1000);
  }
  if(digitalRead(6)==HIGH){
    Serial.write("B5");
    digitalWrite(8,HIGH);
    delay(1000);
    digitalWrite(8,LOW);
    delay(1000);
  }
}