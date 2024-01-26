from hub import port
import motor, motor_pair, color_sensor, runloop, sys

# Constants for Advanced Drive Base
motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
WHEEL_CIRCUMFERENCE = 17.5 # cm – wheel size for DB1

# follow right side of black line (Black-White edge) until distance is covered.
async def line_follow_for_distance_cm(distance_cm):
    # Calculate the number of degrees to turn to cover the desired distance.
    # See lesson on More Accurate Turns for explanation.
    motor_degrees = int((distance_cm/WHEEL_CIRCUMFERENCE) * 360)
    print(motor_degrees)
    # Use motor E for DB1 because it moves clockwise and the degrees count up.
    motor.reset_relative_position(port.E, 0)
    while motor.relative_position(port.E) < motor_degrees :
        if (color_sensor.reflection(port.B) < 50): # sensor is on Black. Adjust threshold as needed if this is too high
            motor_pair.move(motor_pair.PAIR_1, 30, velocity = 200) # Turn right
        else: # sensor is on white
            motor_pair.move(motor_pair.PAIR_1, -30, velocity = 200) # Turn left
        print(motor.relative_position(port.E), end='>')
			
async def main():
	await line_follow_for_distance_cm(17.5)   # ONE 
	sys.exit(0)

runloop.run(main())

## la misurazione della relative_position è ERRATA

