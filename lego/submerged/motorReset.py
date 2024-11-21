from hub import light_matrix, port
import motor

import runloop
import sys

async def main():
    motor.run_to_absolute_position(port.A, 20, 1110)
    await runloop.sleep_ms(1000)   # wait 1 second to allow execute previous command

    motor.run_to_absolute_position(port.A, -20, 1110)
    await runloop.sleep_ms(1000)   # wait 1 second to allow execute previous command

    motor.run_to_absolute_position(port.A, 0, 1110)
    await runloop.sleep_ms(1000)   # wait 1 second to allow execute previous command

runloop.run(main())

sys.exit(0)
