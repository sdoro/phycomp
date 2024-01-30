# test su 3 tiles (Terminatore, Curva, Terminatore): T+C+T

from hub import port
import motor, motor_pair, color_sensor, runloop, sys

# The drive motors are in port A (left) and port E (right).
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# The wheel circumference is 27.63 cm.
WHEEL_CIRCUMFERENCE = 27.63

# rest position for motor moves clockwise
motor.reset_relative_position(port.E, 0)

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50)
async def line_follow_forever(v):

    path = []
    cnt = 0

    while True:
        cnt += 1

        if color_sensor.reflection(port.F) < 30:            # sensore DX indica incrocio?
            break                                           # fermati!
        # Compute the error: please attention to inversion!
        #error = 50 - color_sensor.reflection(port.B)       # il sensore SX (B) segue linea a SX ha BLACK
        error = color_sensor.reflection(port.B) - 50        # il sensore SX (B) segue linea a DX ha BLACK

        # Compute the correction by multiplying the error
        # by a Constant of Proportionality
        myConstant = 4.5
        correction = int(error * 0.5 * myConstant)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)

        if cnt%250 == 0:                                    # save a sample avery 250 loop step
            path.append(motor.relative_position(port.E))

    motor_pair.stop(motor_pair.PAIR_1)
    rp = motor.relative_position(port.E)
    print(round(rp, 2), 'gradi')                            # print lenght track
    lt = rp / 360 * WHEEL_CIRCUMFERENCE
    print(round(lt, 2), 'cm')                               # print lenght track
    print(path)

async def main():
    await line_follow_forever(125)
    sys.exit(0)

runloop.run(main())
