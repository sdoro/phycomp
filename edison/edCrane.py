
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_MEDIUM

#--------Your code below-----------

remoteValue = 0

while True:
    #read remote code 
    remoteValue = Ed.ReadRemote()
    
    #determine which buton is pressed
    if remoteValue == 1:
        # spin the magnetic spool clockwise
        # this will raise or lower the magnet
        Ed.Drive(Ed.FORWARD_LEFT, 2, Ed.DISTANCE_UNLIMITED)
        Ed.TimeWait(50, Ed.TIME_MILLISECONDS)
    elif  remoteValue == 2:
        # spin the magnetic spool counter-clockwise
        #this will raise or lower the magnet
        Ed.Drive(Ed.BACKWARD_LEFT, 2, Ed.DISTANCE_UNLIMITED)
        Ed.TimeWait(50, Ed.TIME_MILLISECONDS)
    elif  remoteValue == 3:
        # spin the crane counter-clockwise
        Ed.Drive(Ed.FORWARD_RIGHT, 3, Ed.DISTANCE_UNLIMITED)
        Ed.TimeWait(50, Ed.TIME_MILLISECONDS)
    elif  remoteValue == 4:
        # spin the crane clockwise
        Ed.Drive(Ed.BACKWARD_RIGHT, 3, Ed.DISTANCE_UNLIMITED)
        Ed.TimeWait(50, Ed.TIME_MILLISECONDS)
    else:
        #no remote code 
        Ed.Drive(Ed.STOP, Ed.SPEED_1, Ed.DISTANCE_UNLIMITED)



