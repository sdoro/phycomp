
import motor
from hub import port, button
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

VALUE = 20
async def main():

    cnt = 0
    while True:
        if button.pressed(button.LEFT):
            await tail(VALUE, DOWN)
            await head(VALUE, DOWN)
            cnt += 1
        if button.pressed(button.RIGHT):
            await head(VALUE, UP)
            await tail(VALUE, UP)
            cnt += 1

        if cnt > 10:              # numero max di attivazioni bottoni SX e DX
            break

    print('fine main')
    sys.exit(0)

runloop.run(*[main()])
