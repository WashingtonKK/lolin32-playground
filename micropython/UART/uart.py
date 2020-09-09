#Importing UART
from machine import UART

#Configuring UART with 9600 baudrate
uart = UART(0, baudrate=9600)

uart.write("Hello")
