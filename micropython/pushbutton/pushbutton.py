import machine
import utime

#Declaring the button with a pull up resistor
#The button is connected on pin 0
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

#Checking button activity
while True:
    #Checking the value of the button on pin 0
    if button.value() == 0:
        print("Button pressed")

    #1 ms delay
    utime.sleep_ms(1)