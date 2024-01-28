WHEEL_CIRCUMFERENCE_DB1 = 17.5  # cm, this is a constant for your robot
WHEEL_CIRCUMFERENCE_ADB = 27.63 # cm, this is a constant for your robot

def degreesForDistance(distance_cm): # input must be in the same unit as WHEEL_CIRCUMFERENCE
    return int((distance_cm/WHEEL_CIRCUMFERENCE_ADB) * 360) # Add multiplier for gear ratio if needed


d = 20
d = float(input('Quanti centimetri? '))
print(degreesForDistance(d))

