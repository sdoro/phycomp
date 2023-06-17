

from machine import Pin, PWM
import time

# Atom Lite
buzzerPin = 26

beeper = PWM(Pin(buzzerPin), freq=440, duty=512)
time.sleep(0.5)

# release the PWM pin
beeper.deinit()

# bot
