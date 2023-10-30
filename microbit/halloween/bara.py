import radio

from microbit import display, Image, button_a, sleep, compass

import random

radio.config(group = 1)

baseline = compass.get_field_strength() # Take a baseline reading of magnetic strength

door = 'closed'
while True:
    sleep(500)
    if abs(compass.get_field_strength() - baseline) < 10000 and door == 'closed':
        # Magnetic field strength increased by 10000
        door = 'opened'
        randomIcon = random.randint(1, 3)
        if randomIcon == 1:
            display.show(Image.ANGRY)
        if randomIcon == 2:
            display.show(Image.GHOST)
        if randomIcon == 3:
            display.show(Image.SKULL)
        radio.send(str(randomIcon))
        print('mandato :', randomIcon)
    elif abs(compass.get_field_strength() - baseline) > 10000 and door == 'opened':
        door = 'closed'
        radio.send('0')
        print('mandato :', 0)
        display.clear()
