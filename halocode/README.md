# using Ubuntu esptool package

$ esptool -p /dev/ttyUSB0 chip_id
```
esptool.py v2.8
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... ESP32
Chip is ESP32D0WDQ6 (revision 1)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: ec:94:cb:5e:19:e8
Enabling default SPI flash mode...
Warning: ESP32 has no Chip ID. Reading MAC instead.
MAC: ec:94:cb:5e:19:e8
Hard resetting via RTS pin...
```

# using esptool installed with pip

$ esptool.py -p /dev/ttyUSB0 chip_id
```
esptool.py v4.4
Serial port /dev/ttyUSB0
Connecting....
Detecting chip type... Unsupported detection protocol, switching and trying again...
Connecting....
Detecting chip type... ESP32
Chip is ESP32-D0WDQ6 (revision v1.0)
Features: WiFi, BT, Dual Core, 240MHz, VRef calibration in efuse, Coding Scheme None
Crystal is 40MHz
MAC: ec:94:cb:5e:19:e8
Uploading stub...
Running stub...
Stub running...
Warning: ESP32 has no Chip ID. Reading MAC instead.
MAC: ec:94:cb:5e:19:e8
Hard resetting via RTS pin...
```

# use of machine.reset() in REPL

```
>>> import machine
>>> machine.reset()
ets Jun  8 2016 00:22:57

rst:0xc (SW_CPU_RESET),boot:0x33 (SPI_FAST_FLASH_BOOT)
configsip: 0, SPIWP:0xee
clk_drv:0x00,q_drv:0x00,d_drv:0x00,cs0_drv:0x00,hd_drv:0x00,wp_drv:0x00
mode:DIO, clock div:2
load:0x3fff0018,len:4
load:0x3fff001c,len:612
load:0x40078000,len:8468
ho 0 tail 12 room 4
load:0x40080400,len:6160
entry 0x40080684
firmware version is:25.01.009
build time: Jan  6 2021, 18:06:02
MicroPython 39860aad-dirty on 2021-01-06; ESP32 module with ESP32
Type "help()" for more information.
>>>
```
# use of os.uname() in REPL

```
>>> import os
>>> os.uname()
(sysname='esp32', nodename='esp32', release='1.11.0', version='39860aad-dirty on 2021-01-06', machine='ESP32 module with ESP32')
```

