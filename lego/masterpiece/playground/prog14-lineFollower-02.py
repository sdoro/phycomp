from hub import port
import motor, motor_pair, color_sensor, runloop, sys

# Constants for Drive Base 1
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50)
async def line_follow_forever(v):
    while (True):
        # Compute the error
        error = 50 - color_sensor.reflection(port.B)
        # Compute the correction by multiplying the error
        # by a Constant of Proportionality
        myConstant = 4
        correction = int(error * 0.5) * myConstant
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)

async def main():
    await line_follow_forever(100)

runloop.run(main())
