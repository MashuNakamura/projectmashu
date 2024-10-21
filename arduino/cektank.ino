#include "handle_container.h"

void CekTank() {

  pinMode(EMPTY_C1, OUTPUT);
  pinMode(FULL_C1, OUTPUT);
  pinMode(EMPTY_C2, OUTPUT);
  pinMode(FULL_C2, OUTPUT);
  for (;;) {
    Serial.println("===================");
    for (int i = 0; i < ARR_SIZE; i++) {
      if (pengisian_tank[i]) {
        if (tank[i] >= VOLUME_AIR_MAKSIMAL){
          pengisian_tank[i] = false;
        } else {
          tank[i] += 250;
        }
      }
          Serial.print("Level Air Saat Ini ");
          Serial.print(i+1);
          Serial.print(" : ");
          Serial.println(tank[i]);
          if (tank[i] <= 0) {
            if (i == 0) digitalWrite(EMPTY_C1, HIGH);
            if (i == 1) digitalWrite(EMPTY_C2, HIGH);
          } else if (tank[i] == VOLUME_AIR_MAKSIMAL) {
            if (i == 0) digitalWrite(FULL_C1, HIGH);
            if (i == 1) digitalWrite(FULL_C2, HIGH);
          } else {
            digitalWrite(FULL_C1, LOW);
            digitalWrite(EMPTY_C1, LOW);
            digitalWrite(FULL_C2, LOW);
            digitalWrite(EMPTY_C2, LOW);
          }
      vTaskDelay( 100 / portTICK_PERIOD_MS );
    }
  }
}
