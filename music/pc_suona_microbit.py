#!/usr/bin/env python3

from rtttl import RTTTL
import songs

import music

def suona(freq, msec):
    music.pitch(int(freq), int(msec))

tune = RTTTL(songs.find('Entertainer'))
for freq, msec in tune.notes():
    suona(freq, msec)

