from machine import ADC
from utime import sleep

IR_sensor = ADC(27)

while True:
    print(IR_sensor.read_u16())
    sleep(0.2)


#600 -> 38000
#square wave with period about 0.5s when light is green