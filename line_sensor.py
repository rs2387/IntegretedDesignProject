from machine import Pin
from utime import sleep

sensor = Pin(28, Pin.IN)

def line_sensor_test():
    while True:
        print(sensor.value())
        sleep(0.2)

line_sensor_test()