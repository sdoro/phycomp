from microbit import *
import music

from rtttl import RTTTL
import songs

# Use spaker.off() to turn off the speaker.
# This does not disable sound output to an edge connector pin.
speaker.off() 

tune = RTTTL(songs.find('TakeOnMe'))

for freq, msec in tune.notes():
    music.pitch(int(freq), int(msec))
    
    