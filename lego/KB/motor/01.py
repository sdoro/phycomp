from spike import PrimeHub

hub = PrimeHub()                  # this is an object

from spike import Motor
from spike.control import wait_for_seconds

# Single motor control
motor1 = Motor("A")

#motor1.start(100)                   # start the motor at speed (-100, 100)
#motor1.start_at_power(100)          # start motor at motor power level (-100%, 100%)
wait_for_seconds(2)                  # waits for 2 seconds
motor1.stop()                        # stop motor

#motor1.run_for_seconds(3, 50)       # run for certain number of seconds
#motor1.run_for_degrees(45, 50)      # run for 45 degrees
#motor1.run_for_rotations(2, 50)     # run for 2 rotations
#motor1.run_to_position(0, 'counterclockwise', 100) # run to the right position

