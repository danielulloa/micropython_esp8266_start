# Instalación de Micropython en ESP8266


Instalar [esptool](https://github.com/espressif/esptool)

Verificar tamaño de la memoria flash con ````esptool flash_id```` 

Borrar memoria flash ````esptool erase_flash```` tambien se puede especificar el puerto si hay mas de un esp8266 conectado.

Descargar micropython desde el [sitio oficial](http://www.micropython.org/download/esp8266/)

Al momento de redactar este documento la versión mas estable es v1.13

## Uso de vscode

instalar [nodejs](https://nodejs.org/es/download/)

instalar [pymakr](https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr) en vscode

editar las opciones globales de pymakr:
````
CTRL+SHIFT+P
Pymakr > Global Settings

````


````json
{
	"address": "COM4",
	"username": "",
	"password": "",
	"sync_folder": "",
	"open_on_start": true,
	"safe_boot_on_upload": false,
	"py_ignore": [
		"pymakr.conf",
		".vscode",
		".gitignore",
		".git",
		"project.pymakr",
		"env",
		"venv"
	],
	"fast_upload": true,
	"sync_file_types": "py,txt,log,json,xml,html,js,css,mpy",
	"ctrl_c_on_connect": true,
	"sync_all_file_types": false,
	"auto_connect": false,
	"autoconnect_comport_manufacturers": [
		"Pycom",
		"Pycom Ltd.",
		"FTDI",
		"Microsoft",
		"Microchip Technology, Inc."
	]
}


````

Instalar [micropy-cli](https://github.com/BradenM/micropy-cli) para gestionar proyectos con Micropython

descargar stubs para esp8266 
````
micropy stubs search esp8266

	MicroPy  Results for esp8266:
	MicroPy  esp8266-micropython-1.10.0
	MicroPy  esp8266-micropython-1.11.0
	MicroPy  esp8266-micropython-1.9.3
	MicroPy  esp8266-micropython-1.9.4
	MicroPy  esp8266-pycopy-1.11.0
	MicroPy  esp8266-pycopy-2.11.0
	MicroPy  esp8266-pycopy-2.11.0.1

micropy stubs add esp8266-micropython-1.11.0

````

Estos archivos se usan para tener IntelliSense, autocompletado y linting en vscode.

Una vez terminada la instalacion inicializar el directorio con ````micropy init````

## Ejemplos

Algunos ejemplos se encuentran en este repositorio

``turnLED.py`` es para prender y apagar un led mediante una función
``blinkMP.py`` inspirado en el ejemplo básico de Arduino, parpadear un led
``pwmLED.py`` implementación de una señal SPWM
``simpleHTTPserver.py`` servidor HTTP
``ledHTTP`` control de un led por interfaz web

## Tips and tricks

#### gpio

El led integrado en la placa nodemcu es el pin 2.

#### memoria libre
````python
import gc
gc.collect()
gc.mem_free()
````

## Referencias

https://lemariva.com/blog/2019/08/micropython-vsc-ide-intellisense

https://forum.micropython.org/viewtopic.php?t=6389

https://github.com/BradenM/micropy-cli