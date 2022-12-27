MicroPython v1.14-876-gfbecba865 on 2021-05-04; LEGO Technic Large Hub with STM32F413xx

$ ampy -p /dev/ttyACM0 ls
/.flash_hash
/.runtime_hash
/_api
/boot.py
/bt-lk1.dat
/bt-lk2.dat
/commands
/etc
/event_loop
/hub_runtime.mpy
/main.py
/mindstorms
/programrunner
/projects
/protocol
/runtime
/sounds
/spike
/system
/ui
/util
/version.py


$ ampy -p /dev/ttyACM0 get /version.py
""" GENERATED """
__version__ = "4.0.0-gecko.7"

$ picocom  /dev/ttyACM0
C-c
MicroPython v1.14-876-gfbecba865 on 2021-05-04; LEGO Technic Large Hub with STM32F413xx
Type "help()" for more information.
>>> 


$ screen /dev/ttyACM0
C-c
MicroPython v1.14-876-gfbecba865 on 2021-05-04; LEGO Technic Large Hub with STM32F413xx
Type "help()" for more information.
>>> 
