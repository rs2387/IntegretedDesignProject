from machine import Pin, Timer

#GPIO15 maps to pin 20, use pin 18 for ground
led = Pin(15, Pin.OUT)
tim = Timer(-1)

def tick(timer):
    led.toggle()

tim.init(freq=2, mode=Timer.PERIODIC, callback=tick)
