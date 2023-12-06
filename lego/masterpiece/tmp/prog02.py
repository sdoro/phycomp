from hub import port
from hub import light_matrix
import runloop
import distance_sensor
import sys

# Function that returns true if an obstacle is found within 5cm
def obstacle_found():
    distance = distance_sensor.distance(port.B)
    # distance must be valid and less than 10cm (100mm)
    return distance > 0 and distance < 100

async def main():

    while True:
        # light off
        pixels = [1] * 4
        distance_sensor.show(port.B, pixels)

        # wait until obstacle found
        await runloop.until(obstacle_found)
        print('rilevato!')

        # light on
        pixels = [50] * 4
        distance_sensor.show(port.B, pixels)

        # Attendi cinque secondi
        await runloop.sleep_ms(5000)

    #sys.exit(0)

runloop.run(main())

