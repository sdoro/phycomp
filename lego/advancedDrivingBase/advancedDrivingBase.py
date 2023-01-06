
from spike import PrimeHub, MotorPair
from spike.control import wait_for_seconds, wait_until
from spike.operator import greater_than, less_than

hub = PrimeHub()
drive_motors = MotorPair('A', 'E')

drive_motors.set_default_speed(50)
drive_motors.set_motor_rotation(27.63, 'cm')

wait_for_seconds(1)

drive_motors.move(20, 'cm')
drive_motors.move(-20, 'cm')
drive_motors.move(20, 'cm', steering=-40)

hub.motion_sensor.reset_yaw_angle()

drive_motors.start(steering=100)
wait_until(hub.motion_sensor.get_yaw_angle, greater_than, 90)
drive_motors.stop()

drive_motors.start(steering=-100)
wait_until(hub.motion_sensor.get_yaw_angle, less_than, 0)
drive_motors.stop()

