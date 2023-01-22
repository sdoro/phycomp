from spike import PrimeHub, MotorPair, Motor, DistanceSensor
from spike.control import wait_for_seconds


hub = PrimeHub()
drive_motors = MotorPair('C', 'D')
grabber_motor = Motor('E')
distance_sensor = DistanceSensor('F')


drive_motors.set_default_speed(30)
drive_motors.set_motor_rotation(17.5, 'cm')
grabber_motor.set_default_speed(-20)
grabber_motor.run_for_seconds(1)
grabber_motor.set_default_speed(20)
grabber_motor.run_for_degrees(75)

hub.speaker.beep(60)
hub.speaker.beep(72)

hub.right_button.wait_until_pressed()

wait_for_seconds(1)

drive_motors.start()
distance_sensor.wait_for_distance_closer_than(10, 'cm')
drive_motors.stop()

grabber_motor.run_for_degrees(-75)

hub.speaker.beep(60)
hub.speaker.beep(72)

drive_motors.move(-20, 'cm')
