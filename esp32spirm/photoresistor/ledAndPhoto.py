
from machine import Pin, PWM, ADC
import time

def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

pwm = PWM(Pin(26,Pin.OUT), 1000)     # led

adc = ADC(Pin(4))                    # fotoresistore
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)

min = 10_000
max = 0

try:
    while True:
        adcValue = adc.read()
        if adcValue < min:
            min = adcValue
        if adcValue > max:
            max = adcValue
          
        scaled = map_range(adcValue, 120, 370, 0, 1023)
        # valori scalati calcolati sulla luce dell'ambiente di test
        pwm.duty(scaled)
        print(adcValue, scaled)     # debug
        time.sleep_ms(100)
except:
    pwm.deinit()
    print("Done")
    print(adcValue, '[', min, ',', max, ']')





