
Use bluetoothctl to enable bluetooth and scanning:

$ sudo bluetoothctl
[bluetooth]# agent on
Agent is already registered
[bluetooth]# default-agent
Default agent request successful
[bluetooth]# scan on
Discovery started


Press the Bluetooth button on SPIKE, in bluetoothctl you should see something like:

[NEW] Device 30:E2:83:05:1E:1D 30:E2:83:05:1E:1D
[CHG] Device 30:E2:83:05:1E:1D Name: LEGO Hub@PROF
[CHG] Device 30:E2:83:05:1E:1D Alias: LEGO Hub@PROF


Now pair with that device:

[bluetooth]# pair 30:E2:83:05:1E:1D
Attempting to pair with 30:E2:83:05:1E:1D
[CHG] Device 30:E2:83:05:1E:1D Connected: yes
[CHG] Device 30:E2:83:05:1E:1D Modalias: bluetooth:v0397p0001d0001
[CHG] Device 30:E2:83:05:1E:1D UUIDs: 00000000-deca-fade-deca-deafdecacaff
[CHG] Device 30:E2:83:05:1E:1D UUIDs: 00001101-0000-1000-8000-00805f9b34fb
[CHG] Device 30:E2:83:05:1E:1D UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device 30:E2:83:05:1E:1D ServicesResolved: yes
[CHG] Device 30:E2:83:05:1E:1D Paired: yes
Pairing successful
[CHG] Device 30:E2:83:05:1E:1D ServicesResolved: no
[CHG] Device 30:E2:83:05:1E:1D Connected: no

List your paired devices:

[bluetooth]# paired-devices
Device 30:E2:83:05:1E:1D LEGO Hub@PROF
[bluetooth]#

Exit out of bluetoothctl and use rfcomm to create a /dev/rfcomm0 device:

$ sudo rfcomm bind 0 40:BD:32:46:9D:3F
$ ls -l /dev/rfcomm0
crw-rw---- 1 root dialout 216, 0 May  3 08:15 /dev/rfcomm0
$

Use screen to connect to /dev/rfcomm0:

$ screen /dev/rfcomm0
MicroPython v1.14-876-gfbecba865 on 2021-05-04; LEGO Technic Large Hub with STM32F413xx
Type "help()" for more information.
>>> {"m":0,"p":[[49, [0, 0, -169, 0]], [61, [99, 7]], [48, [0, 0, 177, 0]], [48, [0, 0, 173, 0]], [49,
{"m":0,"p":[[49, [0, 0, -169, 0]], [61, [99, 7]], [48, [0, 0, 177, 0]], [48, [0, 0, 172, 0]], [49, [0, {"m":0
ctrl-C
>>> import hub
