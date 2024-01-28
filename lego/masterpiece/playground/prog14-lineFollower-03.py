from hub import port
import motor, motor_pair, color_sensor, runloop, sys

# The drive motors are in port A (left) and port E (right).
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)

# The wheel circumference is 27.63 cm.
WHEEL_CIRCUMFERENCE = 27.63

# Follow the right side of black line (Black-White edge).
# To follow a White-Black edge, change the error condition to (reflection - 50).
async def pid_line_follow_forever(v):
    integral = 0
    lastError = 0
    while True:
        if color_sensor.reflection(port.F) < 30:            # sensore DX indica incrocio?
            break                                           # fermati!
        # Compute the error.
        error = 50 - color_sensor.reflection(port.B)
        myConstant = 2.5
        P_fix = error * 0.5 * myConstant
        integral = integral + error
        I_fix = integral * 0.001
        derivative = error - lastError
        lastError = error
        D_fix = derivative * 1
        #I_fix = D_fix = 0
        # clamp the correction from -100 to 100 because SP3 doesn’t seem to do it internally.
        correction = min(100, max(-100, int(P_fix + I_fix + D_fix)))
        # use the correction as the steering
        motor_pair.move(motor_pair.PAIR_1, correction, velocity = v)

    motor_pair.stop(motor_pair.PAIR_1)
    lt = round(motor.relative_position(port.E) / 360 * WHEEL_CIRCUMFERENCE, 2)
    print(lt)                                                                     # print track lenght

async def main():
    await pid_line_follow_forever(250)
    sys.exit(0)

runloop.run(main())
