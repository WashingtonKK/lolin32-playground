from machine import Pin
from time import sleep
from machine import I2C

led = Pin(5, Pin.OUT)

while True:
  #Read state of LED and toggle it.
  led.value(not led.value() )
  #Half second delay
  sleep(0.5)
  
  #Create I2C peripheral with a frequency of 400kHz
  i2c = I2C(freq=400000)
  i2c.scan()
  
  i2c.writeto(42, b'123')
  i2c.readfrom(42, 4)
  
  i2c.readfrom_mem(42, 8, 3)
  
  i2c.writeto_mem(42, 2, b'\x10')
  
