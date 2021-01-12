import machine, time, math

led = machine.PWM(machine.Pin(2), freq = 1000)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep_ms(t)


while True:
    pulse(led,50)