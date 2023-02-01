from microbit import *
from tm1637 import TM1637

tm = TM1637(clk=pin2, dio=pin16)

num = 0
tm.number(num)

while True:
    if button_a.was_pressed():
        num = num + 1
        tm.number(num)
    elif button_b.was_pressed():
        num = num - 1
        tm.number(num)

    if pin_logo.is_touched():
        num = 0
        tm.number(num)

