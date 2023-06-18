
from microbit import *

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

min = 10_000
max = 0

try:
    while True:
        adcValue = pin1.read_analog()
        if adcValue < min:
            min = adcValue
        if adcValue > max:
            max = adcValue
        
        scaled = map_range(adcValue, 0, 550, 0, 1023)
        # valori scalati calcolati sulla luce dell'ambiente di test
        # e sul trimer del led grove
        
        # Output a PWM signal on the pin, with the duty cycle proportional to the provided value.
        # The value may be either an integer or a floating point number between 0 (0% duty cycle) and 1023 (100% duty).
        pin0.write_analog(scaled)
        print(adcValue, scaled)
        
        # wait for 100 milliseconds
        sleep(100)

except:
    print("Done")
    print(adcValue, '[', min, ',', max, ']')
    
# bot
