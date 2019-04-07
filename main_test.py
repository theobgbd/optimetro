###########################################
# OptiMetro : a simple MiniMetro optimiser
# Théo Beigbeder - 2019
# Pierre Boisselier - 2019
##########################################

from interface import *
from interface import T_trains   as trains
import metrics as metrics
import time
import random
import matplotlib.pyplot as plt

### Defining Lines
l_red = Line()
l_red.color = 'red'
l_red.addStation(Station(StationShape.CIRCLE    ,10,   (0,0)))
l_red.addStation(Station(StationShape.SQUARE    ,10,   (1,0)))
l_red.addStation(Station(StationShape.CIRCLE    ,10,   (2,0)))
l_red.addStation(Station(StationShape.TRIANGLE  ,10,   (3,0)))
l_red.addStation(Station(StationShape.CIRCLE    ,10,   (4,0)))

#
l_blue = Line()
l_blue.color = 'blue'
l_blue.addStation(Station(StationShape.CIRCLE   ,10,   (0,1)))
l_blue.addStation(Station(StationShape.SQUARE   ,10,   (1,1)))
l_blue.addStation(Station(StationShape.TRIANGLE ,10,   (1,1)))
l_blue.addStation(l_red.stations[1])
#
l_green = Line()
l_green.color = 'green'
l_green.addStation(Station(StationShape.CROSS   ,10,   (0,2)))
l_green.addStation(Station(StationShape.CIRCLE   ,10,   (1,1)))
l_green.addStation(l_blue.stations[0])
#
#for l in interface.L_lines:
#    print(l.id)

Lines = interface.L_lines
line = l_green.isConnected(StationShape.TRIANGLE,Lines)
print("Connection via ", line)
print(line.color)
# Plotting stations for a giver line
## Populating stations with passengers
#'''
print("* Populating stations")
for l in interface.L_lines :
    for s in l.stations :
        for j in range(1,6) :
            p = s.generatePassenger(limit = 5)

#'''
#print("* Testing connectivity")
#p = Passenger(l_red.stations[0],StationShape.CROSS)
#print(p.travel)
#for i in p.follow:
#    print(i.coord)

### Defining trains ###
trains = [Train(l_blue), Train(l_green), Train(l_red), Train(l_red)]
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

#exit()
#'''
### Main loop ###
master_time = 0
while (P_passengers_alive.__len__() != 0 ) :
    print("-=========-")
    print("Iteration : ", master_time)
    for t in trains :
        print("* Train #",t.id, "arrives in station",t.station, t.line.stations[t.station].shape, "of line", t.line.color)
        # Unboarding loop
        print("\tTrain queue :", len(t.passengers),"/", t.capacity )
        for passenger in t.passengers :
            if (passenger.dest == t.line.stations[t.station].shape):
                t.removePassenger(passenger)
                print("\t> unboarding passenger :", passenger.dest)
            elif (passenger.travel == PassengerTravelFlag.CONNECTION) :
                for l in t.line.stations[t.station].lines :
                    Lines = t.line.stations[t.station].lines
                    a = t.line.isConnected(passenger.dest, Lines)
                    if (a != False and a == l) :
                        t.removePassenger(passenger)
                        print("\t> unboarding connecting passenger :", passenger.dest)

            else :
                print("\t> keeping passenger :", passenger.dest)

        # Boarding loop
        print("\tStation queue :")      # Showing station queue
        for passenger in t.line.stations[t.station].queue :
            Lines = interface.L_lines
            path = []
            print("\t\t",passenger.dest )
            if (t.line.hasShape(passenger.dest) and len(t.passengers) < t.capacity):
                t.addPassenger(passenger)
                passenger.travel = PassengerTravelFlag.DIRECT
                t.line.stations[t.station].removeFromQueue(passenger)
                print("\t> boarding passenger : " , passenger.dest, "for direct ride")

            else :
                for l in t.line.stations[t.station].lines :
                    if (l.hasShape(passenger.dest) == False) :
                        if (t.line.isConnected(passenger.dest, Lines) != None and len(t.passengers) < t.capacity) :
                            t.addPassenger(passenger)
                            passenger.travel = PassengerTravelFlag.CONNECTION
                            t.line.stations[t.station].removeFromQueue(passenger)
                            print("\t> boarding passenger : " , passenger.dest, "for connecting ride")
        t.nextStation()
    # Populating stations
    #for s in interface.S_stations :
    #    for j in range(1,2) :
    #        p = s.generatePassenger(limit = 4)

    print("Global train   load :",metrics.getTrainsLoad(trains))
    print("Global station load :",metrics.getStationsLoad(interface.S_stations))
    metrics.global_load.append(metrics.getTrainsLoad(trains))
    metrics.f_gload.write(str(metrics.global_load[master_time]))
    metrics.f_gload.write("\n")

    for p in interface.P_passengers_alive :
        print(p.dest, p.station)

    countObj()

    master_time = master_time + 1
print(' ----- Done ! ----')
#print(l.hasShape(StationShape.CIRCLE))
#print(S_station_bias.keys(), S_station_bias.values())
#print(s.generatePassenger())
#showAllUUID()
#'''
