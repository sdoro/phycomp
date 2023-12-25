from hub import port
import runloop, motor_pair, sys, color_sensor
# Function that returns true if the intensity is less than 50. This works for a black-white
# mat. If your mat has more colors, use a lower threshold value for black.
def intensity_found():
    return color_sensor.reflection(port.A) < 50

async def main():
    # Set up the pair and start moving
    motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
    motor_pair.move(motor_pair.PAIR_1, 0)
    # wait until intensity found
    await runloop.until(intensity_found)
    # stop and exit
    motor_pair.stop(motor_pair.PAIR_1)

runloop.run(main())
