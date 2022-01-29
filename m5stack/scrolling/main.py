
import uos
from machine import Pin
from neopixel import NeoPixel
from font5 import Font5
from neopixel_scroller import NeopixelScroller
import time

gpio27 = Pin(27, Pin.OUT)
neopixels = NeoPixel(gpio27, 25)
font = Font5()
colors = [(20, 0, 0), (20, 20, 0), (0, 20, 0), (0, 0, 20)]
scroller = None

def randint(low, high):
    s = 0
    bs = uos.urandom(4)
    for b in bs:
        s = (s << 8) | b
    return low + (s % (high - low + 1))

def random_color():
    return colors[randint(0, len(colors) - 1)]

def clear_display():
    global scroller
    scroller = None
    for pixel_index in range(25):
        neopixels[pixel_index] = (0, 0, 0)
    neopixels.write()

def display(message):
    l = len(message)
    for _ in range(1, l*5):
        scroller.scroll()
        neopixels.write()
        time.sleep_ms(300)

message = '0123456789'
color = random_color()
scroller = NeopixelScroller(neopixels, message, font, foreground_color=color)
display(message)
clear_display()

message = 'ABCDEF'
color = random_color()
scroller = NeopixelScroller(neopixels, message, font, foreground_color=color)
display(message)
clear_display()

