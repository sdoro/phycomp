
from machine import Pin, PWM, ADC
import time

pwm = PWM(Pin(26,Pin.OUT), 1000)

adc = ADC(Pin(4))
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
            
        pwm.duty(adcValue)
        #pwm.duty(int(adcValue/20))
        print(adcValue)
        time.sleep_ms(100)
except:
    pwm.deinit()
    print("Done")
    print('[', min, ',', max, ']')





