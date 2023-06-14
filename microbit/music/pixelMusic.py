
from microbit import *
import music

display.clear()

# set central led (2, 2) to high intensity (8)
display.set_pixel(2, 2, 8)

import music
from random import randint

note = "c4:1"
music.play(note)

display.clear()
x = 0
y = 0
notes = ('r4:2', 'g', 'g', 'g', 'eb:8', 'r:2', 'f', 'f', 'f', 'd:8')
for i in range(len(notes)):
    music.play(notes[i])
    display.set_pixel(x, y ,0)    # led DOWN
    x = randint(0, 4)
    y = randint(0, 4)
    display.set_pixel(x, y ,8)    # led UP
    
display.set_pixel(x, y ,0)    # led DOWN
# bot
