import motor
from hub import port
import sys

import runloop

async def wheel(n):
    # vado avanti
    print('motori lanciati!')
    motor.run_for_degrees(port.A, n, -200)
    await motor.run_for_degrees(port.E, n, 200)           # aspetto la terminazione
    print('motori fermati!')


async def main():

    await wheel(180)

    #runloop.run(*[wheel(180)])

    print('fine main')
    sys.exit(0)

runloop.run(*[main()])
