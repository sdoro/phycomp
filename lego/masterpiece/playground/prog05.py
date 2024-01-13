from hub import port, sound
from motor import run_for_time
import runloop, force_sensor, motor_pair, sys
from hub import light_matrix

# Function that returns true if the force sensor is pressed
def force_sensor_pressed():
    return force_sensor.pressed(port.A)


async def contatore():
    cnt = 0

    while True:

        # write your code here
        await light_matrix.write(str(cnt))

        # wait until pressed
        await runloop.until(force_sensor_pressed)
        runloop.run(little(1))
        sound.beep(440, 750, 100)
        await runloop.sleep_ms(500)
        cnt = (cnt+1) % 10



import distance_sensor

# Function that returns true if an obstacle is found within 10cm
def obstacle_found():
    distance = distance_sensor.distance(port.B)
    # distance must be valid and less than 10cm (100mm)
    return distance > 0 and distance < 100

async def distance():

    while True:
        # light off
        pixels = [1] * 4
        distance_sensor.show(port.B, pixels)

        # wait until obstacle found
        await runloop.until(obstacle_found)
        sound.beep(880, 200, 100)
        print('rilevato!')

        # light on
        pixels = [50] * 4
        distance_sensor.show(port.B, pixels)

        runloop.run(little(1))

        # Attendi cinque secondi
        await runloop.sleep_ms(500)



import motor

async def little(n):
    motor.run_for_degrees(port.E, 360*n, 200)
    motor.run_for_degrees(port.F, 360*n, -200)

async def motori():
    runloop.run(little(2))
    sound.beep(880, 200, 100)

async def main():
    c = contatore()
    d = distance()
    #runloop.run(*[c, d]) # anche:
    runloop.run(contatore(),distance(),motori())

runloop.run(main())
