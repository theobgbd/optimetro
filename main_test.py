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
#import matplotlib.pyplot as plt

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
l_green.addStation(Station(StationShape.TRIANGLE   ,10,   (0,2)))
l_green.addStation(Station(StationShape.CIRCLE   ,10,   (1,1)))
l_green.addStation(l_blue.stations[1])
#
l_orange = Line()
l_orange.color = 'orange'
l_orange.addStation(Station(StationShape.CROSS   ,10,   (0,2)))
l_orange.addStation(Station(StationShape.CIRCLE   ,10,   (0,1)))
l_orange.addStation(l_green.stations[1])

#for l in interface.L_lines:
#    print(l.id)
print(l_orange.isConnectedLine(l_orange))
Lines = interface.L_lines
connections = l_orange.isConnected(StationShape.TRIANGLE,Lines,[])
if connections != False :
    for l in connections:
        print(l.color)
else :
    print("no connection")
# Plotting stations for a giver line
## Populating stations with passengers
#'''
print("* Populating stations")
for l in interface.L_lines :
    for s in l.stations :
        for j in range(1,2) :
            p = s.generatePassenger(limit = 5)
#'''
#print("* Testing connectivity")
#p = Passenger(l_red.stations[0],StationShape.CROSS)
#print(p.travel)
#for i in p.follow:
#    print(i.coord)

### Defining trains ###
trains = [Train(l_red), Train(l_blue), Train(l_green), Train(l_orange)]
#
trains[1].reverse = True
trains[2].reverse = True

#exit()
#'''
### Main loop ###
master_time = 0
while (P_passengers_alive.__len__() != 0 ) :
    print("-=========-")
    print("Iteration : ", master_time)

    # Train management
    for t in trains :
        t.nextStation()  #Moving train to next station

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
        print(p.dest, p.station, p.travel)

    countObj()

    master_time = master_time + 1

#print(l.hasShape(StationShape.CIRCLE))
#print(S_station_bias.keys(), S_station_bias.values())
#print(s.generatePassenger())
#showAllUUID()
#'''
