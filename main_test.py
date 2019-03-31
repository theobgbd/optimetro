###########################################
# OptiMetro : a simple MiniMetro optimiser
# Théo Beigbeder - 2019 
# Pierre Boisselier - 2019
##########################################

from interface import *
import time
import random
#import matplotlib.pyplot as plt
#
s = Station(StationShape.CIRCLE,10,(0,0))
l = Line()
l.addStation(s)
l.addStation(Station(StationShape.SQUARE    ,10,   (1,0)))
l.addStation(Station(StationShape.CIRCLE    ,10,   (2,0)))
l.addStation(Station(StationShape.TRIANGLE  ,10,   (3,0)))
l.addStation(Station(StationShape.CIRCLE    ,10,   (4,0)))
l.addStation(Station(StationShape.CROSS     ,10,   (5,0)))
l.addStation(Station(StationShape.CIRCLE    ,10,   (6,0)))

## Population stations with passengers
for i in range(l.nbstations):
    for j in range(2) :
        a = random.randint(1,4)
        if (l.stations[i].shape != StationShape(a)):
            p = Passenger(l.stations[i],StationShape(a))
            l.stations[i].addToQueue(p)
# Define train
trains = [Train(l)]
#trains[0].station = trains[0].line.stations[len(trains[0].line.stations)-1]

# Main loop
master_time = 0
while (master_time <= 24) :
    print("-=========-")
    print("Iteration : ", master_time)
    for i in range(0,len(trains)) :
        t = trains[i]
        print("* Train #",i, "arrives in station",t.station, t.line.stations[t.station].shape)
        # Showing station queue
        print("\t Station queue :")
        for passenger in t.line.stations[t.station].queue :
            print("\t\t",passenger.dest)
        # Unboarding loop
        for passenger in t.passengers :
            if (passenger.dest == t.line.stations[t.station].shape):
                t.removePassenger(passenger)
                print("unboarding passenger :", passenger.dest)
        # Boarding loop
        for passenger in t.line.stations[t.station].queue :
            print("\t\t",passenger.dest )
            if (t.line.hasShape(passenger.dest)):
                t.addPassenger(passenger)
                t.line.stations[t.station].removeFromQueue(passenger)
                print("boarding passenger : " , passenger.dest)
        print("list of passengers in train:")
        for passenger in t.passengers:
            print("\t\t",passenger.dest)
        
        t.nextStation()
    master_time = master_time + 1

for i in l.stations:
    print(i.arrived)
#print(l.hasShape(StationShape.CIRCLE))
#print(S_station_bias.keys(), S_station_bias.values())
#print(s.generatePassenger())
#showAllUUID()
countObj()

# Plotting stations for a giver line
#for i in range(l.nbstations):
#    plt.scatter(l.stations[i].coord[0], l.stations[i].coord[1], marker = switch_mark[l.stations[i].shape], s = 100)
#plt.show()
