
# test su 3 tiles (Terminatore, Curva, Terminatore): T+C+T

from hub import port
import motor, motor_pair, color_sensor, runloop, sys

import time

# reset position for right motor that moves clockwise
motor.reset_relative_position(port.E, 0)

halt = False

async def contaCentimetri():
    global path
    global halt
    global start

    start = time.ticks_ms()
    
    path = []
    halt = False

    while not halt:
        rp = motor.relative_position(port.E)
        e = [rp, time.ticks_ms() - start]
        path.append(e)
        #print('path tmp: ', path)
        await runloop.sleep_ms(200)                    # sleep only this coroutine

    print('contaCentimetri terminata')

# The drive motors are in port A (left) and port E (right).
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# The wheel circumference is 27.63 cm.
WHEEL_CIRCUMFERENCE = 27.63

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50)
async def line_follow_forever(v):
    global path
    global halt

    while True:
        if color_sensor.reflection(port.F) < 30:        # sensore DX indica incrocio?
            break                                        # fermati!
        # Compute the error: please attention to inversion!
        #error = 50 - color_sensor.reflection(port.B)    # il sensore SX (B) segue linea a SX ha BLACK
        error = color_sensor.reflection(port.B) - 50    # il sensore SX (B) segue linea a DX ha BLACK

        # Compute the correction by multiplying the error
        # by a Constant of Proportionality
        myConstant = 4.5
        correction = int(error * 0.5 * myConstant)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)

    motor_pair.stop(motor_pair.PAIR_1)

    halt = True
    await runloop.sleep_ms(2000)                        # sleep to wait other coroutine finished
    lt = motor.relative_position(port.E) / 360 * WHEEL_CIRCUMFERENCE
    print(round(motor.relative_position(port.E),2), 'gradi')                            # print lenght track
    print(round(lt, 2), 'cm')                               # print lenght track
    print('path completo: ', path)

async def main():
    await line_follow_forever(125)

    sys.exit(0)

runloop.run(main(), contaCentimetri())
