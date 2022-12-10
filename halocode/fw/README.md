
# load ESP firmware using espool

	$ esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 firefly_firmware_25_01_004-ht1.bin
```
esptool.py v4.4
Serial port /dev/ttyUSB0
Connecting....
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: ec:94:cb:5e:19:e8
Uploading stub...
Running stub...
Stub running...
Configuring flash size...
Flash will be erased from 0x00001000 to 0x003bffff...
Compressed 3928064 bytes to 1883495...
Wrote 3928064 bytes (1883495 compressed) at 0x00001000 in 167.1 seconds (effective 188.1 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

# connect to REPL

	$ picocom  /dev/ttyUSB0 -b115200
```
[...]
MicroPython f3359b1 on 2019-06-27; ESP32 module with ESP32
[...]
```

# per uscire da picocom

	C-a C-x

# il firmware più aggiornato, chiamato 25_01_009, una volta installato
# NON permette la digitazione al prompt di micropython. Quindi meglio 004
