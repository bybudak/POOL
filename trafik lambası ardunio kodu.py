int kirmizi=2;
int sari=3;
int yesil=4; 

void setup ()
{
  pinMode(kirmizi, OUTPUT);
  pinMode(sari,    OUTPUT);
  pinMode(yesil,   OUTPUT);
}
void loop() {
  digitalWrite(kirmizi,1);
  digitalWrite(sari,0);
   digitalWrite(yesil,0);
  delay(5000);
  digitalWrite(sari,1);
  delay(1500);
    digitalWrite(kirmizi,0);
  digitalWrite(sari,0);
   digitalWrite(yesil,1);
  delay(4000);
  digitalWrite(sari,1);
   digitalWrite(yesil,0);
  delay(1000);
}