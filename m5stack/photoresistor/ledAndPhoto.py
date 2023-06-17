
from machine import Pin, PWM, ADC

adc = ADC(Pin(26))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_10BIT)

import time

min = 10_000
max = 0

pwm = PWM(Pin(32,Pin.OUT), 1000)

try:
    while True:
        adcValue = adc.read()
        if adcValue < min:
            min = adcValue
        if adcValue > max:
            max = adcValue
            
        pwm.duty(adcValue)
        print(adcValue)
        time.sleep_ms(100)
except:
    pwm.deinit()
    print("Done")
    print('[', min, ',', max, ']')




