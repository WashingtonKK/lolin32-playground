/*
 * Program to control the onboard LED (ON/OFF) from ESP32 using Serial Bluetooth
 * Thanks to Neil Kolbans for his efforts in adding the support to Arduino IDE
 * Tutotial: https://circuitdigest.com/microcontroller-projects/using-classic-bluetooth-in-esp32-and-toogle-an-led
 * 
 * Requires Bluetooth Terminal App, eg. this one:
 * https://play.google.com/store/apps/details?id=com.menthoven.arduinoandroid
 * 
 * To set/change the name of the Bluetooth modules, find the line with comment "Name of Bluetooth Module" in setup()
 * and change the name.
 * 
 * More info:
 * https://github.com/espressif/arduino-esp32/tree/master/libraries/BluetoothSerial
 */

#include "BluetoothSerial.h" //Header File for Serial Bluetooth, will be added by default into Arduino

BluetoothSerial BtSerial; // Object for Bluetooth

int led_pin = 22;

void setup() {
  Serial.begin(115200); // Start Serial monitor
  BtSerial.begin("ESP32_LED_Control"); // Name of Bluetooth Module
  Serial.println("Bluetooth Device is Ready to Pair");

  pinMode(led_pin, OUTPUT); // Specify that LED pin is output
}

void loop() {
  if (BtSerial.available()) { // Check if we receive anything from Bluetooth
    char incoming = BtSerial.read(); //Read what we recevive 
    Serial.print("Received:");
    Serial.println(incoming);

    if (incoming == '1') {
        digitalWrite(led_pin, LOW);
        BtSerial.println("LED turned ON");
    }
    else if (incoming == '0') {
        digitalWrite(led_pin, HIGH);
        BtSerial.println("LED turned OFF");
    }
  }
  delay(20);
}
