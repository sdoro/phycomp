from hub import port
import runloop, motor_pair, sys, color_sensor, color

# Function that returns true if the color sensor sees black
def color_found():
    return color_sensor.color(port.A) == color.GREEN

async def main():
    # Set up the pair and start moving
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    motor_pair.move(motor_pair.PAIR_1, 0)
    # wait until color found
    await runloop.until(color_found)
    # stop and exit
    motor_pair.stop(motor_pair.PAIR_1)


runloop.run(main())
