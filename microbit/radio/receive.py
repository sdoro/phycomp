import radio

from microbit import display, Image, button_a, sleep

radio.config(group = 1)

while True:
    incoming = radio.receive()
    if incoming == 'flash':
        display.show(flash, delay = 100, wait = False)
        print('ricevuto!')

