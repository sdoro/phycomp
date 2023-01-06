# To be able to use MotorPair, you must initialize both motors.
from spike import MotorPair

from spike.control import wait_for_seconds

# The left motor is connected to Port C and the right motor is connected to Port D
drive_motors = MotorPair('C', 'D')

drive_motors.set_default_speed(30)
drive_motors.set_motor_rotation(17.5, 'cm')
wait_for_seconds(1)

for x in range(4):
    drive_motors.move(10, 'cm')
    wait_for_seconds(0.5)
    drive_motors.move(182, 'degrees', steering=100)

