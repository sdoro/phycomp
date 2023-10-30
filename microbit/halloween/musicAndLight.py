import radio

from rtttl import RTTTL
import songs

import music

from microbit import *

flag = 0
def suona(freq, msec, pin):
    global flag
    if flag == 0:
        flag = 1
    else:
        flag = 0
    music.pitch(int(freq), int(msec))
    pin.write_digital(flag)


from microbit import display, Image, button_a, sleep

radio.config(group = 1)

while True:
    incoming = radio.receive()
    if incoming == str(1):
        display.show(Image.ANGRY)
        print('ricevuto!', 1)
        tune = RTTTL(songs.find('Indiana'))
        for freq, msec in tune.notes():
            suona(freq, msec, pin1)
        
    if incoming == str(2):
        display.show(Image.GHOST)
        print('ricevuto!', 2)
        tune = RTTTL(songs.find('TopGun'))
        for freq, msec in tune.notes():
            suona(freq, msec, pin2)
            
    if incoming == str(3):
        display.show(Image.SKULL)
        print('ricevuto!', 3)
        tune = RTTTL(songs.find('StarWars'))
        for freq, msec in tune.notes():
            suona(freq, msec, pin1)
            

