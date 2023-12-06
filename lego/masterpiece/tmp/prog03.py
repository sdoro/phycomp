from hub import port
from motor import run_for_time
import runloop, force_sensor, motor_pair, sys
from hub import light_matrix

# Function that returns true if the force sensor is pressed
def force_sensor_pressed():
    return force_sensor.pressed(port.A)

async def main():
    cnt = 0

    while True:

        # write your code here
        await light_matrix.write(str(cnt))

        # wait until pressed
        await runloop.until(force_sensor_pressed)
        await runloop.sleep_ms(500)
        cnt = (cnt+1) % 10

runloop.run(main())
