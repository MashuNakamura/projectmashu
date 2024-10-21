#include "handle_lt.h"

const int RED_PINS[] = {TL1_RED, TL2_RED, TL3_RED, TL4_RED};
const int GREEN_PINS[] = {TL1_GREEN, TL2_GREEN, TL3_GREEN, TL4_GREEN};
const int YELLOW_PINS[] = {TL1_YELLOW, TL2_YELLOW, TL3_YELLOW, TL4_YELLOW};

void MatikanSemuaLampu() {
  for (int i = 0; i < 4; i++) {
    digitalWrite(RED_PINS[i], LOW);
    digitalWrite(GREEN_PINS[i], LOW);
    digitalWrite(YELLOW_PINS[i], LOW);
  }
}

// Function to set a green light and turn on all other red lights
void MenyalakanLampu(int light, int *pinArray) {
  MatikanSemuaLampu();
  for (int i = 0; i < 4; i++) {
    if (pinArray[i] != light) {
      digitalWrite(RED_PINS[i], HIGH);
    }
  }
  digitalWrite(light, HIGH);
}

// Function to initialize pins as OUTPUT
void InisialisasiPins() {
  for (int i = 0; i < 4; i++) {
    pinMode(RED_PINS[i], OUTPUT);
    pinMode(GREEN_PINS[i], OUTPUT);
    pinMode(YELLOW_PINS[i], OUTPUT);
  }
}

void Lever() {
  const int potPin[4] = {A2, A0, A1, A3}; // Analog pin connected to SIG of the potentiometer
  int potValue = 0;     // Variable to store the potentiometer value

  for (;;) {
    for (int i = 0; i < 4; i++) {
      potValue = analogRead(potPin[i]); // Read the potentiometer value
      potValue = (int) (potValue * 0.01) * 10;
      Serial.print("nuel ke ");
      Serial.print(i);
      Serial.print(": ");
      Serial.println(potValue); // Print the potentiometer value to the Serial Monitor

      if (potValue > 50) {
        xQueueSend(potQueue, &i, portMAX_DELAY);
        delay(10000);
      }
    }
    delay(500);
  }
}

void LampuLED() {
  const TickType_t red_delay = 8000 / portTICK_PERIOD_MS;
  const TickType_t yellow_delay = 4000 / portTICK_PERIOD_MS;
  int index = -1;

  InisialisasiPins();

  for (;;) {
    for (int i = 0; i < 4; i++) {
      for (;;) {
        if (xQueueReceive(potQueue, &index, 0) == pdPASS) {
          MenyalakanLampu(GREEN_PINS[index], GREEN_PINS);
          vTaskDelay(red_delay);

          MenyalakanLampu(YELLOW_PINS[index], YELLOW_PINS);
          vTaskDelay(yellow_delay);
          if (xQueueReceive(potQueue, &index, 0) == pdPASS) {
            MenyalakanLampu(GREEN_PINS[index], GREEN_PINS);
            vTaskDelay(red_delay);

            MenyalakanLampu(YELLOW_PINS[index], YELLOW_PINS);
            vTaskDelay(yellow_delay);
            continue;
          }
          break;
        }
        break;
      }

      MenyalakanLampu(GREEN_PINS[i], GREEN_PINS);
      vTaskDelay(red_delay);

      MenyalakanLampu(YELLOW_PINS[i], YELLOW_PINS);
      vTaskDelay(yellow_delay);
    }
    MatikanSemuaLampu();
  }
}
