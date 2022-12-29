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


$ screen /dev/ttyACM0
C-c
MicroPython v1.14-876-gfbecba865 on 2021-05-04; LEGO Technic Large Hub with STM32F413xx
Type "help()" for more information.
>>> import os
>>> os.uname()
(sysname='LEGO Technic Large Hub', nodename='LEGO Learning System Hub', release='1.14.0', version='v1.14-876-gfbecba865 on 2021-05-04', machine='LEGO Technic Large Hub with STM32F413xx')


$ ampy -p /dev/ttyACM0 get /version.py
""" GENERATED """
__version__ = "4.0.0-gecko.7"


Dopo aggiornamento:

$ picocom  /dev/ttyACM0
C-c
MicroPython 1b7af80af on 2022-11-29; SPIKE Prime with STM32F413
Type "help()" for more information.
>>> import os
>>> os.uname()
(sysname='SPIKE', nodename='SPIKE', release='1.19.1', version='1b7af80af on 2022-11-29', machine='SPIKE Prime with STM32F413')

