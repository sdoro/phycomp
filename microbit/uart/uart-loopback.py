
from microbit import *

# If tx and rx are not specified then the internal USB-UART TX/RX pins are used
# which connect to the USB serial converter on the micro:bit, thus connecting the
# UART to your PC. You can specify any other pins you want by passing the desired
# pin objects to the tx and rx parameters.

uart.init(baudrate=115200)    #
printed = False

while True:
    if button_a.is_pressed():
        display.show("A")
        print("button A", end="")
        uart.write(",AAA")
        printed = True

    if button_b.is_pressed():
        display.show("B")
        print("button B", end="")
        uart.write(",BBB")
        printed = True

    sleep(2000)
    if printed:
        display.show(" ")
        print()
        printed = False

# in REPL mode, we can see the print() output followed by uart.write() output
