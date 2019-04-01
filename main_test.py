###########################################
# OptiMetro : a simple MiniMetro optimiser
# Théo Beigbeder - 2019
# Pierre Boisselier - 2019
##########################################

from interface import *
import time
import random
import matplotlib.pyplot as plt

### Defining Lines
l_red = Line()
l_red.addStation(Station(StationShape.CIRCLE    ,10,   (0,0)))
l_red.addStation(Station(StationShape.SQUARE    ,10,   (1,0)))
l_red.addStation(Station(StationShape.CIRCLE    ,10,   (2,0)))
l_red.addStation(Station(StationShape.TRIANGLE  ,10,   (3,0)))
l_red.addStation(Station(StationShape.CIRCLE    ,10,   (4,0)))
#
l_blue = Line()
l_blue.addStation(Station(StationShape.CIRCLE    ,10,   (0,1)))
l_blue.addStation(Station(StationShape.SQUARE     ,10,   (1,1)))
l_blue.addStation(Station(StationShape.TRIANGLE     ,10,   (1,1)))
l_blue.addStation(l_red.stations[4])
#
l_green = Line()
l_green.addStation(Station(StationShape.CROSS    ,10,   (0,2)))
l_green.addStation(l_blue.stations[2])
#
for l in interface.L_lines:
    print(l.id)

print(l_red.isConnectedLine(l_green))
print(l_red.isConnected(StationShape.CROSS,interface.L_lines))


# Plotting stations for a giver line
## Populating stations with passengers
for l in interface.L_lines :
    for i in range(l.nbstations):
        for j in range(1) :
            a = random.randint(1,4)
            if (l.stations[i].shape != StationShape(a)):
                p = Passenger(l.stations[i],StationShape(a))
                l.stations[i].addToQueue(p)

### Defining trains ###
trains = [Train(l_blue), Train(l_blue), Train(l_red), Train(l_red)]

#
trains[1].reverse = True
trains[1].nextStation()
trains[1].nextStation()
trains[1].nextStation()
#
trains[2].reverse = True
trains[2].nextStation()
trains[2].nextStation()
trains[3].nextStation()

exit()
### Main loop ###
master_time = 0
while (P_passengers_alive.__len__() != 0 ) :
    print("-=========-")
    print("Iteration : ", master_time)
    for t in trains :
        print("* Train #",t.id, "arrives in station",t.station, t.line.stations[t.station].shape, "of line", t.line.id)
        # Showing station queue
        print("\tStation queue :")
        for passenger in t.line.stations[t.station].queue :
            print("\t\t",passenger.dest)
        # Unboarding loop
        for passenger in t.passengers :
            if (passenger.dest == t.line.stations[t.station].shape):
                t.removePassenger(passenger)
                print("\t> unboarding passenger :", passenger.dest)
        # Boarding loop
        for passenger in t.line.stations[t.station].queue :
            print("\t\t",passenger.dest )
            if (t.line.hasShape(passenger.dest)):
                t.addPassenger(passenger)
                t.line.stations[t.station].removeFromQueue(passenger)
                print("\t> boarding passenger : " , passenger.dest, "for direct ride")

            elif (t.line.isConnected(passenger.dest)):


                # for line in lines :
                #     if (t.line.isConnected(line)):
                #         if (line.hasShape(passenger.dest)):
                #             t.addPassenger(passenger)
                #             t.line.stations[t.station].removeFromQueue(passenger)
                #             print("\t> boarding passenger : " , passenger.dest, "for transit ride")

        t.nextStation()
    #time.sleep(1)
    for i in range(l.nbstations):
        for j in range(1) :
            if (bool(random.getrandbits(1)) and bool(random.getrandbits(1))):
                a = random.randint(1,2)
                if (l.stations[i].shape != StationShape(a)):
                    l.stations[i].addToQueue(Passenger(l.stations[i],StationShape(a)))
    master_time = master_time + 1

#print(l.hasShape(StationShape.CIRCLE))
#print(S_station_bias.keys(), S_station_bias.values())
#print(s.generatePassenger())
#showAllUUID()
#countObj()
