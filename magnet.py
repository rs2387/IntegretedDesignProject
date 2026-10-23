from machine import ADC
from utime import sleep

hall_effect = ADC(26)

while True:
    print(hall_effect.read_u16())
    sleep(0.2)

def get_magnet():
    return(hall_effect.read_u16())

#25000 -> 40000 -> 55000
#south is low, north is high