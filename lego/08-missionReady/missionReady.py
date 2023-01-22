from spike import Motor, MotorPair
from spike.control import wait_for_seconds


dozer_blade_motor = Motor('C')
lift_arm_motor = Motor('D')
drive_motors = MotorPair('A', 'E')


drive_motors.set_default_speed(25)
drive_motors.set_motor_rotation(27.63, 'cm')


dozer_blade_motor.start(-100)
lift_arm_motor.start(-100)
wait_for_seconds(1)
dozer_blade_motor.stop()
lift_arm_motor.stop()

dozer_blade_motor.run_for_degrees(70, speed=100)
lift_arm_motor.run_for_degrees(20, speed=100)

drive_motors.move(-2, 'cm')
drive_motors.move(10.5, 'cm')

dozer_blade_motor.run_for_degrees(180, speed=40)

drive_motors.move(-6, 'cm')

dozer_blade_motor.run_for_degrees(-180, speed=60)
dozer_blade_motor.run_for_degrees(180, speed=60)

drive_motors.move(7, 'cm')

dozer_blade_motor.run_for_degrees(-180, speed=60)

drive_motors.move(0.405, 'rotations', steering=-100)
drive_motors.move(60.5, 'cm', steering=-30)
drive_motors.move(34, 'cm')
drive_motors.move(32, 'cm', steering=-50)
drive_motors.move(17.5, 'cm')
drive_motors.move(0.415, 'rotations', steering=-100)
drive_motors.move(32, 'cm')
