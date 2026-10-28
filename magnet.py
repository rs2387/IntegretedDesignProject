from machine import ADC
from utime import sleep

hall_effect = ADC(26)



def get_magnet():
    value = hall_effect.read_u16()
    if value < 40500:
        pole = "north"
        return pole
    elif value > 42500:
        pole = "north"
        return pole
    else:
        pole = get_magnet()
    

#40500 -> 42000 -> 42500
#south is low, north is high