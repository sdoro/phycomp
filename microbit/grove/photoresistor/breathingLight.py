from microbit import *

while True:
    for i in range(0, 1023, 1):
       pin0.write_analog(i)
       sleep(1)
       
    for i in range(1023, 0, -1):
       pin0.write_analog(i)
       sleep(1)