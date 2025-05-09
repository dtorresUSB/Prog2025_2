// Definir la variable para el número a enviar
int numero = 0;

void setup() {
  // Iniciar el puerto serie a 9600 baudios
  Serial.begin(9600);
}

void loop() {
  // Enviar el número por el puerto serie
  Serial.println(numero);

  // Incrementar el número
  numero++;

  // Esperar 1 segundo antes de enviar el siguiente número
  delay(1000);
}

