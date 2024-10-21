#include "handle_input.h"

void CekSwitch() {
  pinMode(PUMP_SWITCH, INPUT);
  pinMode(PUMP, OUTPUT);
  for (;;) {
    if (digitalRead(PUMP_SWITCH) == HIGH) {
        tank[index_tank] -= 25;
        if (tank[0] > VOLUME_AIR_MAKSIMAL || tank[0] == 0) {
          tank[0] = 0;
          pengisian_tank[0] = true;
          index_tank = 1;
        }
        if (tank[1] > VOLUME_AIR_MAKSIMAL || tank[1] == 0) {
          tank[1] = 0;
          pengisian_tank[1] = true;
          index_tank = 0;
        }
        if (index_tank == 1) {
          pengisian_tank[1] = false;
        } else {
          pengisian_tank[0] = false;
        }
        digitalWrite(PUMP, HIGH);

    } else {
      digitalWrite(PUMP, LOW);
    }
    vTaskDelay( 50 / portTICK_PERIOD_MS );
  }
}
