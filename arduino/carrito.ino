void setup() {
  Serial.begin(9600);

  // Configura tus pines de motores aquí
  pinMode(2, OUTPUT); // Motor A
  pinMode(3, OUTPUT); // Motor B
}

void loop() {
  if (Serial.available() > 0) {
    String comando = Serial.readStringUntil('\n');

    if (comando == "avanzar") {
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
    } else if (comando == "retroceder") {
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
    } else if (comando == "izquierda") {
      digitalWrite(2, LOW);
      digitalWrite(3, HIGH);
    } else if (comando == "derecha") {
      digitalWrite(2, HIGH);
      digitalWrite(3, LOW);
    } else if (comando == "piloto") {
      // Lógica de piloto automático
    }
  }
}
