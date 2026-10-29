from machine import ADC, Pin
from led import led
from utime import sleep

hall_effect = ADC(26)

red_led = led(10)
green_led = led(12)

def get_magnet():
    value = hall_effect.read_u16()
    if value < 40500:
        pole = "south"
        red_led.off()
        green_led.on()
        return pole
    elif value > 42500:
        pole = "north"
        green_led.off()
        red_led.on()
        return pole
    else:
        pole = get_magnet()
    

#40500 -> 42000 -> 42500
#south is low, north is high