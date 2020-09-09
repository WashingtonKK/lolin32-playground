from machine import Pin
from time import sleep

#Assign the led to pin 5
led = Pin(5, Pin.OUT)

while True:
    #We are turning the LED on and off at an iterval of 1 second
    led.on()
    sleep(1)
    led.off()
    sleep(1)
