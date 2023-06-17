
from microbit import *

min = 10_000
max = 0

try:
    while True:
        adcValue = pin1.read_analog()
        print(adcValue)
        if adcValue < min:
            min = adcValue
        if adcValue > max:
            max = adcValue
            
        # Output a PWM signal on the pin, with the duty cycle proportional to the provided value.
        # The value may be either an integer or a floating point number between 0 (0% duty cycle) and 1023 (100% duty).
        pin0.write_analog(adcValue)

        # wait for 100 milliseconds
        sleep(100)

except:
    print("Done")
    print('[', min, ',', max, ']')
    
# bot
