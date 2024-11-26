from hub import light_matrix, port, sound
import motor

import runloop
import sys

async def main():
    '''
    Stall detection allowed the code to move on to the next line even when the motor got
    stuck (unable to complete its move). The beep played even though the motor did not
    finish completing its command.
    https://primelessons.org/en/ProgrammingLessons/MovingObjectsStall.pdf
    '''

    motor.run_to_absolute_position(port.A,  40, 1110)
    await runloop.sleep_ms(1000)   # wait 1 second to allow execute previous command
    await sound.beep()

    motor.run_to_absolute_position(port.A, -40, 1110)
    await runloop.sleep_ms(1000)   # wait 1 second to allow execute previous command
    await sound.beep()

    motor.run_to_absolute_position(port.A,   0, 1110)
    await runloop.sleep_ms(1000)   # wait 1 second to allow execute previous command
    await sound.beep()

runloop.run(main())

sys.exit(0)
