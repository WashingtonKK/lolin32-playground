from machine import Pin

#Create a GPIO pin and assign it relay
#The pin to control the relay
relay = Pin(0, Pin.OUT)

while True:
    if True:    #Condition to evaluate whether to turn relay on or off
        relay.on() # Setting relay to on
    else relay.off()

