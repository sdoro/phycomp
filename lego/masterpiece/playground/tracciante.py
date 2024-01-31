
# test su 3 tiles (Terminatore, Curva, Terminatore): T+C+T

from hub import port, button
import motor, motor_pair, color_sensor, runloop, sys

import time

# The drive motors are in port A (left) and port E (right).
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# The wheel circumference is 27.63 cm.
WHEEL_CIRCUMFERENCE = 27.63

# Questa funzione restituisce `True` se si preme il pulsante sinistro.
def left_pressed():
    return button.pressed(button.LEFT) > 0

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50)
async def line_follow_forever(v):
    global path
    global halt

    # reset position for right motor that moves clockwise
    motor.reset_relative_position(port.E, 0)

    start = time.ticks_ms()
    path = [[0, 0]]

    while True:
        rp = motor.relative_position(port.E)
        cond = (rp < 1250) or (rp > 1450)
        if color_sensor.reflection(port.F) < 30:
            break
        if color_sensor.reflection(port.F) < 30 and cond:        # sensore DX indica incrocio?
            break
            rp = motor.relative_position(port.E)
            break
            if (rp < 1250) or (rp > 1450):
                motor_pair.stop(motor_pair.PAIR_1)
                print('trovato arresto: ', rp)
                break                                        # fermati!
        # Compute the error: please attention to inversion!
        #error = 50 - color_sensor.reflection(port.B)    # il sensore SX (B) segue linea a SX ha BLACK
        error = color_sensor.reflection(port.B) - 50    # il sensore SX (B) segue linea a DX ha BLACK

        # Compute the correction by multiplying the error
        # by a Constant of Proportionality
        myConstant = 4.5
        correction = int(error * 0.5 * myConstant)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)
        if left_pressed():
            rp = motor.relative_position(port.E)
            t = time.ticks_ms() - start
            if (rp - path[-1][0]) > 25:    # troppo vicini? non registro
                path.append([rp, t])

    motor_pair.stop(motor_pair.PAIR_1)

    lt = motor.relative_position(port.E) / 360 * WHEEL_CIRCUMFERENCE
    print(round(motor.relative_position(port.E),2), 'gradi')                            # print lenght track
    print(round(lt, 2), 'cm')                            # print lenght track
    print(time.ticks_ms() - start, 'msec')            # print lenght time
    print('path percorso: ', path)

async def main():
    await line_follow_forever(125)

    #sys.exit(0)

runloop.run(main())
