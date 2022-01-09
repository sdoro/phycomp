from m5stack import *
from m5ui import *
from uiflow import *
import time

rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


face = -1



import random



def buttonA_wasPressed():
  global face
  face = random.randint(1, 6)
  if face == 6:
    rgb.set_screen([0xFFFFFF,0,0xFFFFFF,0,0xFFFFFF,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xFFFFFF,0,0xFFFFFF,0,0xFFFFFF])
  if face == 5:
    rgb.set_screen([0xFFFFFF,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0xFFFFFF])
  if face == 4:
    rgb.set_screen([0xFFFFFF,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0xFFFFFF])
  if face == 3:
    rgb.set_screen([0,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0])
  if face == 2:
    rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0,0,0])
  if face == 1:
    rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0,0,0xFFFFFF,0,0,0,0,0,0,0,0,0,0,0,0])
  wait(0.5)
  pass
btnA.wasPressed(buttonA_wasPressed)


rgb.setBrightness(2)
rgb.set_screen([0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00,0,0x00ff00,0,0x00ff00,0,0,0,0x00ff00,0,0,0])

