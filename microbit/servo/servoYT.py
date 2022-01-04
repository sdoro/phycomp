
# https://support.microbit.org/support/solutions/articles/19000101864-using-a-servo-with-the-micro-bit
# https://www.youtube.com/watch?v=k4iM5fXt54k

from microbit import *

# Servo control:
#  50 = ~1 millisecond pulse all right
#  75 = ~1,5 millisecond pulse all center
# 100 = ~2 millisecond pulse left

period = 20
pin0.set_analog_period(period)               # The minimum valid value is 1ms.
pin0.write_analog(1)

center = 80                                  # initial setup
delta = 50

left = center - delta
right = center + delta

while True:

    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.SKULL)
        break

    if button_a.is_pressed():
        delta = 750
        pin0.write_analog(center)            # center
        display.show(Image.ARROW_N)
        sleep(delta)
        pin0.write_analog(left)              # SX or Est
        display.show(Image.ARROW_E)
        sleep(delta)
        pin0.write_analog(center)            # center
        display.show(Image.ARROW_N)
        sleep(delta)
        pin0.write_analog(right)             # DX or West
        display.show(Image.ARROW_W)
        sleep(delta)
        pin0.write_analog(center)            # center
        display.show(Image.ARROW_N)
        sleep(delta)

    # from zero to 180
    if pin_logo.is_touched():
        delta = 500
        min = 30
        max = 130
        for i in range(min+2,max+2,5):
            pin0.write_analog(i)
            print(i)
            sleep(delta)
        break

    # move random
    from random import randint
    if button_b.is_pressed():
        delta = 350
        r = 15
        pin0.write_analog(randint(-r,r)+center)            # center
        display.show(Image.ARROW_N)
        sleep(delta)
        pin0.write_analog(randint(-r,r)+left)              # SX or Est
        display.show(Image.ARROW_E)
        sleep(delta)
        pin0.write_analog(randint(-r,r)+center)            # center
        display.show(Image.ARROW_N)
        sleep(delta)
        pin0.write_analog(randint(-r,r)+right)             # DX or West
        display.show(Image.ARROW_W)
        sleep(delta)
        pin0.write_analog(randint(-r,r)+center)            # center
        display.show(Image.ARROW_N)
        sleep(delta)
    sleep(200)

pin0.write_analog(30)
