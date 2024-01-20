from hub import port
import motor_pair, runloop, sys, math

from hub import sound

# Constants for Advanced Drive Base
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
WHEEL_CIRCUMFERENCE = 27.63            # cm - please adjust according to your robot wheel
TRACK = 14.6                           # cm - please measure your own robot.
SPIN_CIRCUMFERENCE = TRACK * math.pi

async def spin_turn(robot_degrees, motor_speed):
    # Add a multiplier for gear ratios if you’re using gears
    motor_degrees = int((SPIN_CIRCUMFERENCE/WHEEL_CIRCUMFERENCE) * abs(robot_degrees))
    if robot_degrees > 0:
        # spin clockwise
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, motor_degrees, 100, velocity=motor_speed)
    else:
        #spin counter clockwise
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, motor_degrees, -100, velocity=motor_speed)

async def main():

    sound.volume(70)

    # Spin 90 clockwise with speed 200
    await spin_turn(90, 200)
    #await runloop.sleep_ms(1000)
    await sound.beep(400, 1000)        # replaced previous line with sound and same delay 

    # Spin 90 counterclockwise with speed 200
    await spin_turn(-90, 200)
    #await runloop.sleep_ms(1000)
    await sound.beep(600, 1000)        # replaced previous line with sound and same delay

    # Spin 45 clockwise with speed 300
    await spin_turn(45, 300)
    #await runloop.sleep_ms(1000)
    await sound.beep(800, 1000)        # replaced previous line with sound and same delay

    # Spin 45 counterclockwise with speed 300
    await spin_turn(-45, 300)
    #await runloop.sleep_ms(1000)
    await sound.beep(1000, 1000)       # replaced previous line with sound and same delay

    # stop and exit the program
    sys.exit(0)

runloop.run(main())
