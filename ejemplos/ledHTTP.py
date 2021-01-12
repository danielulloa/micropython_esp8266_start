import socket
import gc
from machine import Pin

LED = Pin(2,Pin.OUT)

def pagina_web():
    if LED.value() == 1:
        estadoLED = "<h1>ON</h1>"
    else:
        estadoLED = "OFF"

    html = """<!DOCTYPE html>
    <html>
        <head>
            <title>Raspberry Rack</title>
            <style>
            h1 {color: blue;}
            </style>
        </head>
        <body> <h1 align="center">Panel de control</h1>
            <p align="center">Estado del LED: <strong>""" + estadoLED + """</strong></p>
            <p align="center"><a href=/?LED=ON><button>ON</button></a></p>
            <p align="center"><a href=/?LED=OFF><button>OFF</button></a></p>
        </body>
    </html>
    """

    return html

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('',80))
s.listen(5)

while True:
    cl, addr = s.accept()
    request = cl.recv(1024)
    request = str(request)
    LED_ON = request.find('/?LED=ON')
    LED_OFF = request.find('/?LED=OFF')
    if LED_ON == 6:
        LED.value(1)
    if LED_OFF == 6:
        LED.value(0)
    response = pagina_web()
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)
    cl.close()
    gc.collect()    