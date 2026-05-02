#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
Servo servo6;
int q[6];

void setup() {
  Serial.begin(9600);
  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);
  servo5.attach(10);
  servo6.attach(11);

  for (int i = 0; i < 6; i++) {
    q[i] = 90;
  }

  mover_servos();
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');

    procesar_datos(data);
    mover_servos();
  }
}

void procesar_datos(String data) {
  sscanf(data.c_str(),
         "Q1:%d,Q2:%d,Q3:%d,Q4:%d,Q5:%d,Q6:%d",
         &q[0], &q[1], &q[2], &q[3], &q[4], &q[5]);
}

void mover_servos() {
  servo1.write(q[0]);
  servo2.write(q[1]);
  servo3.write(q[2]);
  servo4.write(q[3]);
  servo5.write(q[4]);
  servo6.write(q[5]);
}
