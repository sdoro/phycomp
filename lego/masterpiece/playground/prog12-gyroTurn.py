from hub import port, motion_sensor
import runloop, motor_pair, sys
# GLOBALS
# Set from -355 to 355. Positive numbers are clockwise.
degrees_to_turn = 0
# Yaw angle reading that indicates the robot needs to stop
stop_angle = 0

# Function that returns true when the yaw has turned past stop angle
def turn_done():
    global degrees_to_turn, stop_angle
    # convert tuple decidegree into the same format as in app and blocks
    yaw_angle = motion_sensor.tilt_angles()[0] * -0.1
    # if we need to turn less than 180 degrees, check the absolute values
    if (abs(degrees_to_turn) < 180):
        return abs(yaw_angle) > stop_angle
    # If we need to turn more than 180 degrees, compute the yaw angle we need to stop at.
    if degrees_to_turn >= 0: # moving clockwise
    # The adjusted yaw angle is positive until we cross 180.
    # Then, we are negative numbers counting up.
        return yaw_angle < 0 and yaw_angle > stop_angle
    else:
    # The adjusted yaw angle is negative until we cross 180
    # Then, we are positive numbers counting down.
        return yaw_angle > 0 and yaw_angle < stop_angle

async def setupMotors():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    motion_sensor.reset_yaw(0)
    await runloop.until(motion_sensor.stable)

async def spinTurn(degrees):
    if abs(degrees) > 355:
        print("Out of range")
        return
    await setupMotors()
    global degrees_to_turn, stop_angle
    degrees_to_turn = degrees # set the global to use in the turn_done function
    # set the stop_angle global to use in the turn_done function
    if (abs(degrees) < 180):
        stop_angle = abs(degrees_to_turn)
    else:
        stop_angle = (360 - abs(degrees)) if degrees < 0 else (abs(degrees) - 360)
    # set the steering laue based on turn direction
    steering_val = 100 if degrees >= 0 else -100
    motor_pair.move(motor_pair.PAIR_1, steering_val, velocity=200)
    await runloop.until(turn_done)
    motor_pair.stop(motor_pair.PAIR_1)

async def main():

    await spinTurn(30)
    await runloop.sleep_ms(500)

    motor_pair.unpair(motor_pair.PAIR_1)    # la coppia è già fissata: altrimenti errore
    await spinTurn(-30)

    sys.exit("Done")

runloop.run(main())

