
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

per uscire da picocom: C-a C-x

il firmware più aggiornato, chiamato 25_01_009, una volta installato
NON permette la digitazione al prompt di micropython. Quindi meglio lo 004


# test di micropython standard

dopo aver letto https://eaceto.dev/2020/03/22/micropython-on-an-esp32/
ho provato e funziona. L'articolo descrive la versione 1.12 e mostr
come alzare la frequenza. Funziona tutto.

```
$ esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
esptool.py v4.4
Serial port /dev/ttyUSB0
Connecting.......
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: ec:94:cb:5e:19:e8
Uploading stub...
Running stub...
Stub running...
Erasing flash (this may take a while)...
Chip erase completed successfully in 10.6s
Hard resetting via RTS pin...
```

```
$ esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 /tmp/x/esp32-idf4-20191220-v1.12.bin 
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
Flash will be erased from 0x00001000 to 0x00158fff...
Compressed 1408512 bytes to 894711...
Wrote 1408512 bytes (894711 compressed) at 0x00001000 in 78.9 seconds (effective 142.8 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

```
$ picocom  /dev/ttyUSB0 -b115200
[...]
>>> 
MPY: soft reboot
MicroPython v1.12 on 2019-12-20; ESP32 module with ESP32
Type "help()" for more information.
>>> import machine
>>> machine.freq()
160000000
>>> machine.freq(240000000)
I (71200) pm_esp32: Frequency switching config: CPU_MAX: 240, APB_MAX: 240, APB_MIN: 240, Light sleep: DISABLED
>>> machine.freq()
240000000
```

# updated to current micropython v1.20.0

```
>>> 
MPY: soft reboot
MicroPython v1.20.0 on 2023-04-26; ESP32 module with ESP32
Type "help()" for more information.
>>> 
```

# il firmware 25_01_004

Sembrerebbe un pò duro a dare il promt ma forse perchè con
un thread fa il gioco di luci.

```
>>> 
PYB: soft reboot
MicroPython 39860aad-dirty on 2021-01-06; ESP32 module with ESP32
Type "help()" for more information.
```

Per conoscere la versione firmware (per firefly_firmware_25_01_004-ht1.bin invece vale 25.01.004):

```
>>> import makeblock
makeblock.get_firmware_version()
'25.01.009'
```

L'ultimo firmware, ossia il 25.01.009, si riesce a caricare da Windows e tramite il programma mblock.

