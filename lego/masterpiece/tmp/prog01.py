
import motor
from hub import port

import runloop

async def little(n):
    await motor.run_for_degrees(port.E, 360*n, 200)
    motor.run_for_degrees(port.F, 360*n, -200)

async def bigger(n):
    motor.run_for_degrees(port.C, 360*(n-1), 200)
    motor.run_for_degrees(port.D, 360*(n-1), -200)


async def main():

    #await little(2)
    #await bigger(2)

    l = little(3)
    b = bigger(2)
    #runloop.run(*[l,b])
    
    print('fine main')


#runloop.run(*[main(),little(2),bigger(1)])
#l = little(3)
#b = bigger(2)
#m = main()
runloop.run(*[main(),little(3),bigger(2)])
