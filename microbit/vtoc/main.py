
from microbit import *
from sgp30 import SGP30

sgp30 = SGP30()

sgp30.iaq_init()

print(sgp30.serial)
print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0
while True :
    eCO2 = sgp30.eCO2()
    TVOC = sgp30.TVOC()
    print("eCO2 = %d ppm \t TVOC = %d ppb" % (eCO2, TVOC))
    sleep(1000)
    elapsed_sec += 1
    if elapsed_sec > 10:
        elapsed_sec = 0
        print("**** Baseline values: eCO2 = 0x%X, TVOC = 0x%X" % (sgp30.baseline_eCO2(), sgp30.baseline_TVOC()))
