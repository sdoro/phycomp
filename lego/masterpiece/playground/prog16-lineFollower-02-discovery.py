# test su 3 tiles (Terminatore, Curva, Terminatore): T+C+T

from hub import port
import motor, motor_pair, color_sensor, runloop, sys

import time

global path
path = list()
global stop
stop = False

async def contaCentimetri(nPort):
    while not stop:
        e = [motor.relative_position(nPort), time.ticks_ms()]
        print(e)
        path.append(e)
        await runloop.sleep_ms(1_000)                    # sleep only this coroutine


# The drive motors are in port A (left) and port E (right).
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# The wheel circumference is 27.63 cm.
WHEEL_CIRCUMFERENCE = 27.63

# reset position for right motor that moves clockwise
motor.reset_relative_position(port.E, 0)

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50)
async def line_follow_forever(v):
    while True:
        if color_sensor.reflection(port.F) < 30:         # sensore DX indica incrocio?
            break                                        # fermati!
        # Compute the error: please attention to inversion!
        #error = 50 - color_sensor.reflection(port.B)    # il sensore SX (B) segue linea a SX ha BLACK
        error = color_sensor.reflection(port.B) - 50     # il sensore SX (B) segue linea a DX ha BLACK

        # Compute the correction by multiplying the error
        # by a Constant of Proportionality
        myConstant = 4.5
        correction = int(error * 0.5 * myConstant)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)

    motor_pair.stop(motor_pair.PAIR_1)
    lt = motor.relative_position(port.E) / 360 * WHEEL_CIRCUMFERENCE
    print(round(lt, 2), 'cm')                            # print lenght track
    print('path: ', path)

async def main():
    runloop.run(contaCentimetri(port.E))                 # start coroutine
    await line_follow_forever(225)
    stop = True
    await runloop.sleep_ms(1_100)                        # sleep to wait other coroutine finished
    
    sys.exit(0)

runloop.run(main())
