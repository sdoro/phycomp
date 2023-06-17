from rtttl import RTTTL
import songs

from machine import Pin, PWM
import time

# Atom Lite
buzzerPin = 26

tone = PWM(Pin(buzzerPin), freq=440, duty=512)

def play_tone(freq, msec):
    #print('freq = {:6.1f} msec = {:6.1f}'.format(freq, msec))
    if freq > 0:
        tone.duty(10)
        tone.freq(int(freq))

    time.sleep(msec*0.001)  # Play for a number of msec
    tone.duty(0)            # Stop playing
    time.sleep(0.01)        # Delay 50 ms between notes
    
tune = RTTTL(songs.find('TakeOnMe'))

for freq, msec in tune.notes():
    play_tone(freq, msec)

tone.deinit() 

# bot