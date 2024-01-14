import motor_pair
from hub import port
import sys, runloop

async def pivot(ms):
    # dx (left, right = 200, 0)
    motor_pair.move_tank(motor_pair.PAIR_1, 200, 0)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

    await runloop.sleep_ms(ms)

    # sx (left, right = 0, 200)
    motor_pair.move_tank(motor_pair.PAIR_1, 0, 200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

async def spin(ms):
    # dx (left, right = 200, -200)
    motor_pair.move_tank(motor_pair.PAIR_1, 200, -200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

    await runloop.sleep_ms(ms)

    # sx (left, right = -200, 200)
    motor_pair.move_tank(motor_pair.PAIR_1, -200, 200)
    await runloop.sleep_ms(ms)
    motor_pair.stop(motor_pair.PAIR_1)

async def main():

    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

    #await pivot(500)
    await spin(500)

    print('fine main')
    sys.exit(0)

runloop.run(*[main()])

