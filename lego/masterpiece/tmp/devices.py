import hub
import runloop

# Il modulo device consente di scrivere codice per ottenere informazioni sui dispositivi collegati all'hub.
import device

import errno

async def main():

    print(hub.device_uuid())            # 03970000-3500-2C00-1350-504D59363920
    print(hub.hardware_id())            # E

    # devs
    devs = []
    devs.append(device.id(hub.port.A))  # medium motor #49
    try:
        devs.append(device.id(hub.port.B))  # color sensor #48
    except OSError:
        devs.append([])
   
    devs.append(device.id(hub.port.C))  # color sensor #48
    devs.append(device.id(hub.port.D))  # large motor  #61
    devs.append(device.id(hub.port.E))  # medium motor #49
    devs.append(device.id(hub.port.F))  # large motor  #61
    print(devs)

    data = []
    data.append(device.data(hub.port.A))
    try:
        data.append(device.data(hub.port.B))
    except OSError:
        data.append([])
    data.append(device.data(hub.port.C))
    data.append(device.data(hub.port.D))
    data.append(device.data(hub.port.E))
    data.append(device.data(hub.port.F))
    print(data)

    while True:
        try:
            print(device.data(hub.port.B))
        except OSError:
            print([])
        await runloop.sleep_ms(1000)

runloop.run(main())

