#Code to enable the on board push button
#The button will be used to terminate any program in the esp32 chip
#This then brings us back to REPL in the event that the chip is stuck

import machine
import sys
import utime

#Define pins
#We are turning on the internal pull-up resistor
repl_button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

#Waiting for the button press
#After the button press, we exit
while True:

    #If the button is pressed, we get back to REPL
    if repl_button.value() == 0:
        print("Getting back to REPL...")
        sys.exit()

    utime.sleep_ms(1)