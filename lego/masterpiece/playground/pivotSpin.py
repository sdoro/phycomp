import motor_pair
from hub import port
import sys, runloop

async def pivot(ms):
    # dx (steering= +50)
    motor_pair.move(motor_pair.PAIR_1, 50, velocity=200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

    await runloop.sleep_ms(ms)

    # sx (steering= -50)
    motor_pair.move(motor_pair.PAIR_1, -50, velocity=200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

async def spin(ms):
    # dx (steering= +100)
    motor_pair.move(motor_pair.PAIR_1, 100, velocity=200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

    await runloop.sleep_ms(ms)

    # sx (steering= -100)
    motor_pair.move(motor_pair.PAIR_1, -100, velocity=200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

async def main():

    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    #await pivot(500)
    await spin(500)

    print('fine main')
    sys.exit(0)

runloop.run(*[main()])

