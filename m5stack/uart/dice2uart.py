from m5stack import *
from m5ui import *
from uiflow import *
import time

rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])


face = None



import random


# Describe this function...
def lancio2():
  global face
  face = random.randint(1, 6)
  if face == 6:
    rgb.set_screen([0xff0000,0,0xff0000,0,0xff0000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xff0000,0,0xff0000,0,0xff0000])
  if face == 5:
    rgb.set_screen([0xff0000,0,0,0,0xff0000,0,0,0,0,0,0,0,0xff0000,0,0,0,0,0,0,0,0xff0000,0,0,0,0xff0000])
  if face == 4:
    rgb.set_screen([0xff0000,0,0,0,0xff0000,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0xff0000,0,0,0,0xff0000])
  if face == 3:
    rgb.set_screen([0,0,0,0,0xff0000,0,0,0,0,0,0,0,0xff0000,0,0,0,0,0,0,0,0xff0000,0,0,0,0])
  if face == 2:
    rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0xff0000,0,0,0,0xff0000,0,0,0,0,0,0,0,0,0,0])
  if face == 1:
    rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0,0,0xff0000,0,0,0,0,0,0,0,0,0,0,0,0])
  uart1.write((str(str(face)) + str('\r')))
  wait(0.5)

# Describe this function...
def lancio():
  global face
  face = random.randint(1, 6)
  if face == 6:
    rgb.set_screen([0x00ff00,0,0x00ff00,0,0x00ff00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0x00ff00,0,0x00ff00])
  if face == 5:
    rgb.set_screen([0x00ff00,0,0,0,0x00ff00,0,0,0,0,0,0,0,0x00ff00,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00])
  if face == 4:
    rgb.set_screen([0x00ff00,0,0,0,0x00ff00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00])
  if face == 3:
    rgb.set_screen([0,0,0,0,0x00ff00,0,0,0,0,0,0,0,0x00ff00,0,0,0,0,0,0,0,0x00ff00,0,0,0,0])
  if face == 2:
    rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0x00ff00,0,0,0,0,0,0,0,0,0,0])
  if face == 1:
    rgb.set_screen([0,0,0,0,0,0,0,0,0,0,0,0,0x00ff00,0,0,0,0,0,0,0,0,0,0,0,0])
  uart1.write((str(str(face)) + str('\r')))
  wait(0.5)


def buttonA_wasPressed():
  global face
  lancio()
  wait(1)
  lancio2()
  wait(1)
  rgb.set_screen([0,0,0,0,0,0,0,0,0,0xffff00,0,0,0,0xffff00,0,0xffff00,0,0xffff00,0,0,0,0xffff00,0,0,0])
  pass
btnA.wasPressed(buttonA_wasPressed)


uart1 = machine.UART(1, tx=26, rx=32)
uart1.init(115200, bits=8, parity=None, stop=1)
rgb.setBrightness(30)
rgb.set_screen([0,0,0,0,0,0,0,0,0,0xffff00,0,0,0,0xffff00,0,0xffff00,0,0xffff00,0,0,0,0xffff00,0,0,0])

