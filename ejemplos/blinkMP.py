import time
from machine import Pin, Signal

led_pin = Pin(2, Pin.OUT)
led = Signal(led_pin, invert=True)

def toggle(p):
    p.value(not p.value())

while True:
    toggle(led)
    time.sleep_ms(500)