from spike import PrimeHub, Motor


hub = PrimeHub()
lift_arm_motor = Motor('D')
dozer_blade_motor = Motor('C')


lift_arm_motor.set_default_speed(-100)
lift_arm_motor.run_for_seconds(1)
dozer_blade_motor.set_default_speed(-100)
dozer_blade_motor.run_for_seconds(1)

lift_arm_motor.set_default_speed(100)
lift_arm_motor.run_for_degrees(70)
dozer_blade_motor.set_default_speed(100)
dozer_blade_motor.run_for_degrees(70)
hub.speaker.beep()

lift_arm_motor.run_for_degrees(180)
lift_arm_motor.run_for_degrees(-180)
dozer_blade_motor.run_for_degrees(180)
dozer_blade_motor.run_for_degrees(-180)
hub.speaker.beep()

lift_arm_motor.run_for_degrees(180, speed=15)
lift_arm_motor.run_for_degrees(-180, speed=15)
dozer_blade_motor.run_for_degrees(180, speed=15)
dozer_blade_motor.run_for_degrees(-180, speed=15)
