# using M5STACK_ATOM-20230426-v1.20.0.bin

# https://github.com/micropython/micropython/blob/master/ports/esp32/boards/M5STACK_ATOM/modules/atom.py

import atom

al = atom.Lite()
#                      R  G  B
#                      v  v  v
al.set_pixel_color(0, 50,50,50)
#                  ^
#                  led button

# bot
