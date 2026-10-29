from machine import Pin, Timer

class led:
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        self.timer = Timer(-1)
        self.led.off()

    def flash(self, interval=500):
        self.timer.deinit()
        self.timer.init(
            period=interval,
            mode=Timer.PERIODIC,
            callback=self._toggle
        )

    def _toggle(self, timer):
        self.led.toggle()

    def on(self):
        self.timer.deinit()
        self.led.on()

    def off(self):
        self.timer.deinit()
        self.led.off()