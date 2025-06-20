// Pines de sensores
const int sensorIzq = 10; // Sensor izquierdo
const int sensorDer = 11; // Sensor derecho

// Pines del puente H L298N
const int IN1 = 2;
const int IN2 = 3;
const int ENA = 5;

const int IN3 = 7;
const int IN4 = 8;
const int ENB = 9;

void setup() {
  // Configurar pines de sensores
  pinMode(sensorIzq, INPUT);
  pinMode(sensorDer, INPUT);

  // Configurar pines del motor
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);

  // Iniciar motores detenidos
  detener();
}

void loop() {
  int izq = digitalRead(sensorIzq);
  int der = digitalRead(sensorDer);

  if (izq == 0 && der == 0) {
    // Ambos sensores ven blanco: seguir recto
    avanzar();
  } else if (izq == 1 && der == 0) {
    // Sensor izquierdo ve negro: girar a la izquierda
    girarIzquierda();
  } else if (izq == 0 && der == 1) {
    // Sensor derecho ve negro: girar a la derecha
    girarDerecha();
  } else {
    // Ambos sensores ven negro: detener o girar
    detener();
  }
}

// Funciones de movimiento
void avanzar() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 150);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, 150);
}

void girarIzquierda() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, 150);
}

void girarDerecha() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 150);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, 0);
}

void detener() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, 0);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, 0);
}