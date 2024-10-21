#include <Arduino_FreeRTOS.h>
#include <semphr.h>
#include "const.h"
#include "handle_input.h"
#include "handle_container.h"

static bool pengisian_tank[ARR_SIZE] = {false, false};
static size_t tank[ARR_SIZE] = {VOLUME_AIR_MAKSIMAL, VOLUME_AIR_MAKSIMAL};
static size_t index_tank = 0;

void setup() {

  Serial.begin(38400);

  xTaskCreate(CekTank, // Task function
              "Pengecekan Tank", // Task name for humans
              128, 
              NULL, // Task parameter
              1, // Task priority
              NULL);
  xTaskCreate(CekSwitch, // Task function
              "Pengecekan Switch", // Task name for humans
              128, 
              NULL, // Task parameter
              2, // Task priority
              NULL);
}

void loop() {}
