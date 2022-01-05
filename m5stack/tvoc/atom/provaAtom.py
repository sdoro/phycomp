
from machine import Pin, I2C

I2C_SCL_GPIO = const(32)     
I2C_SDA_GPIO = const(26)     
I2C_FREQ = const(100000)

# gripping
I2C_SCL_GPIO = const(26)     
I2C_SDA_GPIO = const(0)     
I2C_FREQ = const(400000)


i2c = I2C(
    scl = Pin(I2C_SCL_GPIO, Pin.OUT),
    sda = Pin(I2C_SDA_GPIO, Pin.OUT),
    freq = I2C_FREQ
)

from sgp30 import SGP30

sgp30 = SGP30(i2c)
sgp30.initialise_indoor_air_quality()

while True :
	# acquiring data
        eco2, tvoc = sgp30.indoor_air_quality
        
        # Matrix
        # MicroPython v1.12-36-gf68fe753b-dirty on 2020-01-14; ESP32 module with ESP32
        
        # Lite
        # MicroPython v1.12-36-gf68fe753b-dirty on 2020-01-14; ESP32 module with ESP32
        
        
        
from machine import I2C, Pin
i2c = I2C(scl=Pin(32), sda=Pin(26))

# disable all 8 channels
i2c.writeto(0x70, b'\x00')
i2c.scan()
# [112] - the TCA9548A

# enable channel 0 (SD0,SC0)
i2c.writeto(0x70, b'\x01')
i2c.scan()
# [88, 112] - TVOC/eCO2 & TCA9548A

# enable channel 8
i2c.writeto(0x70, b'\x80')


# The hub itself has an I2C address of 0x70. But by writing data to this address,
# we can select which channel we want to open or close on the fly. When we plug
# in devices with conflicting I2C addresses, we can simply adjust the desired channels
# prior to transmitting data as usual. In doing so, we ensure that there is technically
# only one ‘active’ device at a given I2C address, hence eliminating the conflict.



