# To be able to use MotorPair, you must initialize both motors.
from spike import MotorPair

from spike.control import wait_for_seconds

# The left motor is connected to Port C and the right motor is connected to Port D
drive_motors = MotorPair('C', 'D')

# Sets the default motor speed. The value will be set to "-100" or "100". Default 100
drive_motors.set_default_speed(20)

# Set the distance that the robot travels for one rotation of its wheels.
# The value 17.6 comes from the diameter of the wheel (5.6cm) multiplied by "π" (3.1415).
drive_motors.set_motor_rotation(17.6, 'cm')

# Activate the brakes when the robot stops. The other conditions are 'hold' and 'coast'.
motor_pair.set_stop_action('brake')

wait_for_seconds(1)              # Wait for one second.

for x in range(4):

    # Start both motors simultaneously to move a Driving Base.
    # Steering = "0" makes the Driving Base go straight. 
    # Negative numbers make the Driving Base turn left. Positive numbers make the Driving Base turn right.
    drive_motors.move(10, 'cm')

    wait_for_seconds(0.5)

    # If the value of steering is equal to "-100" or "100," the Driving Base will perform a
    # rotation on itself (i.e., "tank move") at the default speed of each motor.
    # When the "unit" is "rotations" or "degrees," the "amount" parameter value specifies
    # how much the motor axle will turn before stopping.
    drive_motors.move(182, 'degrees', steering = 100)

