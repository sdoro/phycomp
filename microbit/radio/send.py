import radio

from microbit import display, Image, button_a, sleep

radio.config(group = 1)

while True:
    if button_a.was_pressed():
        radio.send('flash')
        print('mandato flash')
