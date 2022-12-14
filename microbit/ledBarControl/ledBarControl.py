from microbit import *

# from https://github.com/rcolistete/Plots_MicroPython_Microbit
def plot_bar_pixels(value, pixelscale, fromtop = False):
    for y in range(5):
        for x in range(5):
            if fromtop:
                yl = y
            else:
                yl = 4-y
            diff = value - ((x + 1) + y*5)*pixelscale
            if diff >= 0:
                display.set_pixel(x, yl, 9)
            else:
                display.set_pixel(x, yl, 0)


while True:
    v = pin0.read_analog()
    print(v)
    plot_bar_pixels(v,1024/25)
