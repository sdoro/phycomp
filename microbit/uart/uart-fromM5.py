
from microbit import uart, sleep, display, pin8, pin12, button_a, button_b

uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx = pin8, rx = pin12)
msgStr = 'empty'

while True:
    if uart.any():
        sleep(100)
        msgByte = uart.read()
        msgStr = str(msgByte, 'UTF-8')
        print("> " + msgStr[0])
        display.scroll("> " + msgStr[0])

    if button_a.is_pressed():
        display.show("X")
        break

    sleep(500)

# return control to USB UART
uart.init(baudrate=115200)
print("> " + msgStr)
