
import motor
from hub import port
import sys

import runloop

UP = True
DOWN = not UP

async def tail(n, direction):
    if direction == UP:
        await motor.run_for_degrees(port.C, n, +200)
    else:
        await motor.run_for_degrees(port.C, n, -200)

async def head(n, direction):
    if direction == UP:
        await motor.run_for_degrees(port.D, n, +200)
    else:
        await motor.run_for_degrees(port.D, n, -200)

VALUE = 40
async def main():
    
    #await head(VALUE, UP)                                # ONE AT TIME
    #await tail(VALUE, DOWN)                              # ONE AT TIME
    #await head(VALUE, DOWN)                              # ONE AT TIME
    #await tail(VALUE, UP)                                # ONE AT TIME

    runloop.run(*[head(VALUE, UP),tail(VALUE, DOWN)])     # SIMULTANEUS
    runloop.run(*[head(VALUE, DOWN),tail(VALUE, UP)])     # SIMULTANEUS

    print('fine main')
    sys.exit(0)               

runloop.run(*[main()])
