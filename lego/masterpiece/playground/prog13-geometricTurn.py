from hub import port
import motor_pair, runloop, sys, math

# Constants for Drive Base 1
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
WHEEL_CIRCUMFERENCE = 17.5 # cm - please adjust according to your robot wheel
TRACK = 14.5 # cm - please measure your own robot.
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
    # Spin 180 clockwise with speed 200
    await spin_turn(180, 200)
    await runloop.sleep_ms(1000)
    # Spin 180 counterclockwise with speed 200
    await spin_turn(-180, 200)
    await runloop.sleep_ms(1000)
    # Spin 90 clockwise with speed 300
    await spin_turn(90, 300)
    # stop and exit the program
    sys.exit("Stopping")

runloop.run(main())
