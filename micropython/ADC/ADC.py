#Importing machine
#Importing ADC
from machine import ADC
from machine import Pin
from time import sleep

#Create an ADC object on pin 32
adc = ADC(Pin(32))

#Setting 11dB input attenuation (Voltage between 0 and 3.6v)
adc.atten(ADC.ATTN_11DB)

#setting 9 bit return values to receive values between 0 and 511
adc.width(ADC.WIDTH_9BIT)

while True:
    #Reading the analog value
    #GPIO pin 32 is connected to a potentiometer
    val = adc.read()
    print(val)
    sleep(1)
