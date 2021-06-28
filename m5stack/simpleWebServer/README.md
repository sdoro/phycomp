
# [Simple web server on ESP32 using MicroPython](https://embedded-things.blogspot.com/2020/08/simple-web-server-on-esp32-using.html)

Alla data di oggi (28.06.2021) la versione di MicroPython che ho usato è la d8d847d62-dirty del 2021-06-04 scaricabile dal sito di M5Stack come UIFlow_Matrix-v1.7.8.bin.

Le modifiche apportate per farla funzionare sono state depositate tramite git e riguardano la connessione con il wifi (non solo user e password ma anche le call). Mi sono aiutato dall'help() stesso che presenta la scheda al prompt:

```
Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection
```

La pagina web riporta:

```
Hello, MicroPython@ESP32!
sysname: esp32
nodename: esp32
release: 1.12.0
version: d8d847d62-dirty on 2021-06-04
machine: M5Stack with ESP32


('192.168.1.110', 46784)
```


