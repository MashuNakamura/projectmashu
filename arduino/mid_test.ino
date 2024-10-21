// What is Mutex used for?
// Mutex is virtual "lock" that help control access to share resources or data between different tasks
// Example : We have two task on arduino, Task 1 is read data from sensor, Task 2 is display that data on LCD
// Mutex is a tool for controling access to shared source in real time system, ensuring only one taskcan access them at time

// Include Necessary Arduino FreeRTOS library
#include <Arduino_FreeRTOS.h>

// Include mutex support
#include <semphr.h>

//   Creating a global variable of type SemaphoreHandle_t with the name mutex

SemaphoreHandle_t mutex;

// Globalcount variable start from 0 
int globalCount = 0;

// Create the Setup, this is the place where Arduino to get started
void setup() {

//        (communication speed) for data transmission between the Arduino board and a connected device, typically 
//        a computer, another Arduino board, or a serial interface module.

  Serial.begin(9600);

// Create mutex, if success then continue
  mutex = xSemaphoreCreateMutex();
  if (mutex != NULL) {
    Serial.println("Mutex created");
  }

// Create tasks

  xTaskCreate(TaskMutex, // Task function
              "Task1", // Task name for humans
              128, //Stack size
              1000, // Task parameter (delay satuan milisecond)
              1, // Task priority
              NULL); // Handler

// This exactly like on the top, but different Task
  xTaskCreate(TaskMutex, // Task function
              "Task2", // Task name
              128, // Stack size
              1000, // Task parameter (delay satuan milisecond)
              1, // Task priority 
              NULL); // Handler

}

// Why is empty? because using FreeRTOS Libary, if we dont use FreeRTOS, then the entire function goes to void loop 
void loop() {}

// Create multiple tasks execute, the TaskMutex function will not return anything and accept pointer as an argument
// Because its void

void TaskMutex(void *pvParameters)
{
  TickType_t delayTime = *((TickType_t*)pvParameters); // Use task parameters to define delay

// Loop forever until there is break statement
  for (;;)
  {

// This is task mutex 
// mutex is handler, then 10 is tick onTime and make sure the value is true, if not they will be false
    if (xSemaphoreTake(mutex, 10) == pdTRUE)
    {
      Serial.print(pcTaskGetName(NULL)); // Why NULL? It because we want to query the name of the calling task. 
      Serial.print(", Count read value: "); // Print message ", Count read value: "
      Serial.print(globalCount); // Print the current task

// The globalcount will increase
      globalCount++;

      Serial.print(", Updated value: "); // output message
      Serial.print(globalCount); // The output will display after increase the variable (example Task 0 upd Task 1)

      Serial.println(); // print new line
            
// xSemaphoreGive gives unlock or access the (TaskMutex)
      xSemaphoreGive(mutex);
    }

// This for Task Delay
// delayTime is delay it self and the port tick is the fourth parameter xTaskCreate
    vTaskDelay(delayTime / portTICK_PERIOD_MS);
  }
}
