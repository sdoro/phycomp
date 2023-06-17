
from microbit import *

while True:
   value = pin1.read_analog()
   print(value)
   if value>=400:
       pin0.write_digital(1)
   else:
       pin0.write_digital(0)
   sleep(1)
# bot