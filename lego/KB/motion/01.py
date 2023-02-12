from spike import PrimeHub

hub = PrimeHub()                  # this is an object

while True:
    print(
        'yaw:',hub.motion_sensor.get_yaw_angle(), 
        'pitch:', hub.motion_sensor.get_pitch_angle(),
        'roll:', hub.motion_sensor.get_roll_angle()
        )
