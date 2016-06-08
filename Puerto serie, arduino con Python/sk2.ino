int x = 0;    // variable
 
void setup() {
  Serial.begin(9600);      // abre el puerto serie a 9600 bps:    
}
 
void loop() {
 
  Serial.println(random(-10, 200)); // Escribe en el puerto un numero aleatorio de -10 a 200
  delay(2000);
}
