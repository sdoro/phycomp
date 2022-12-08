# using Ubuntu esptool

	esptool -p /dev/ttyUSB0 chip_id
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

# using esptool installed using pip

	esptool.py -p /dev/ttyUSB0 chip_id
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

