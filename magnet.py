from machine import ADC
from utime import sleep

hall_effect = ADC(26)



def get_magnet():
    value = hall_effect.read_u16()
    if value < 25000:
        pole = "south"
    elif value > 55000:
        pole = "north"
    else:
        pole = get_magnet()
    return pole

#25000 -> 40000 -> 55000
#south is low, north is high