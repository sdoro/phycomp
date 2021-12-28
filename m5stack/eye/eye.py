#--- M5-spooky-eye.py                ---#
#--- Written by tommyho510@gmail.com ---#
#--- for M5Stick-C (160 x 80 pixels) ---#
#--- Version 1.0 (October 2019)      ---#

from m5stack import *
from m5ui import *
from uiflow import *

from random import randint

lcd.setRotation(1)
setScreenColor(0x000000)
image0 = M5Img(0, 0, "res/eye2-50.jpg", True)

eyefs= [50, 20, 10, 30, 60, 61, 62, 63, 64, 65, 80, 90, 70, 50, 20, 10, 30, 60, 80, 90, 70]
eyers= [1000, 100, 1000, 100, 1000, 20, 100, 20, 20, 20, 100, 1000, 100, 1000, 100, 1000, 100, 100, 100, 1000, 100]
while True:
  for j in range(21):
    image0.changeImg("res/eye2-"+str(eyefs[j])+".jpg")
    if eyers[j] == 1000:
      wait_ms(randint(700,1301))
    else:
      wait_ms(eyers[j])
  wait_ms(2)

