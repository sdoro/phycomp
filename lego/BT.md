

Enable Bluetooth from terminal:


```
bluetoothctl power on
rfkill unblock bluetooth
```


Use bluetoothctl to enable bluetooth and scanning:

```
$ sudo bluetoothctl
[bluetooth]# agent on
Agent is already registered
[bluetooth]# default-agent
Default agent request successful
[bluetooth]# scan on
Discovery started
```


Press the Bluetooth button on SPIKE, in bluetoothctl you should see something like:

```
[NEW] Device 30:E2:83:04:A2:96 30:E2:83:05:1E:1D
[CHG] Device 30:E2:83:04:A2:96 Name: LEGO Hub@PROF
[CHG] Device 30:E2:83:04:A2:96 Alias: LEGO Hub@PROF
```


Now pair with that device:

```
[bluetooth]# pair 30:E2:83:04:A2:96
Attempting to pair with 30:E2:83:04:A2:96
[CHG] Device 30:E2:83:04:A2:96 Connected: yes
[CHG] Device 30:E2:83:04:A2:96 Modalias: bluetooth:v0397p0001d0001
[CHG] Device 30:E2:83:04:A2:96 UUIDs: 00000000-deca-fade-deca-deafdecacaff
[CHG] Device 30:E2:83:04:A2:96 UUIDs: 00001101-0000-1000-8000-00805f9b34fb
[CHG] Device 30:E2:83:04:A2:96 UUIDs: 00001200-0000-1000-8000-00805f9b34fb
[CHG] Device 30:E2:83:04:A2:96 ServicesResolved: yes
[CHG] Device 30:E2:83:04:A2:96 Paired: yes
Pairing successful
[CHG] Device 30:E2:83:04:A2:96 ServicesResolved: no
[CHG] Device 30:E2:83:04:A2:96 Connected: no
```

List your paired devices:

```
[bluetooth]# paired-devices
Device 30:E2:83:04:A2:96 LEGO Hub@PROF
[bluetooth]#
```

Exit out of bluetoothctl:
```
[bluetooth]# quit
```

Use rfcomm to create a /dev/rfcomm0 device (serial):

```
$ sudo rfcomm bind 0 30:E2:83:04:A2:96
$ ls -l /dev/rfcomm0
crw-rw---- 1 root dialout 216, 0 May  3 08:15 /dev/rfcomm0
$
```

Use screen to connect to /dev/rfcomm0 (just done sudo adduser $USER dialout?):

```
$ screen /dev/rfcomm0
MicroPython v1.14-876-gfbecba865 on 2021-05-04; LEGO Technic Large Hub with STM32F413xx
Type "help()" for more information.
>>> {"m":0,"p":[[49, [0, 0, -169, 0]], [61, [99, 7]], [48, [0, 0, 177, 0]], [48, [0, 0, 173, 0]], [49,
{"m":0,"p":[[49, [0, 0, -169, 0]], [61, [99, 7]], [48, [0, 0, 177, 0]], [48, [0, 0, 172, 0]], [49, [0, {"m":0
ctrl-C
>>> import hub
```

To escape the screen (and the shell), you type ctrl + a, and then :quit

You can also transfer file (upload) in Spike and run it with the following command:

```
ampy --port /dev/rfcomm0 run test.py
```

When you are done using the Spike, my suggestion would be to release the port:

```
sudo rfcomm release 0
```

Also:

```
bluetoothctl remove 30:E2:83:04:A2:96
bluetoothctl disconnect 30:E2:83:04:A2:96
```

Put in a script:

```
bluetoothctl -- pair 30:E2:83:04:A2:96
sleep 10
bluetoothctl -- trust 30:E2:83:04:A2:96
bluetoothctl -- connect 30:E2:83:04:A2:96
sleep 5
```

