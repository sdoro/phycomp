from microbit import *
import music

from random import randint

display.clear()

# Use off() to turn off the speaker.
# This does not disable sound output to an edge connector pin.
speaker.off()

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