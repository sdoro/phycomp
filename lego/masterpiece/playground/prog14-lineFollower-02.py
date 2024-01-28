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
    while True:
        if color_sensor.reflection(port.F) < 30:              # sensore DX indica incrocio?
            break                                             # fermati!
        # Compute the error
        error = 50 - color_sensor.reflection(port.B)          # il sensore SX segue linea
        # Compute the correction by multiplying the error
        # by a Constant of Proportionality
        myConstant = 2.5
        correction = int(error * 0.5 * myConstant)
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)

    motor_pair.stop(motor_pair.PAIR_1)
    print(motor.relative_position(port.E))                     # print path lenght

async def main():
    await line_follow_forever(250)
    sys.exit(0)

runloop.run(main())

