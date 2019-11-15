int val =0;
long randnumb;
int analogPin = 2;
void setup() {
  
  Serial.begin(9600); 
  Serial.print("Arduino counter: ");
  delay(50);
  
}

void loop() {
  val = analogRead(analogPin);
  //randnumb = random(150,600);
  //delay(500);
  Serial.println(val);
  //delay(700); // wait half a sec
}

