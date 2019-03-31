###########################################
# OptiMetro : a simple MiniMetro optimiser
# Théo Beigbeder - 2019
# Pierre Boisselier - 2019
##########################################

from interface import * 

s = Station(StationShape.CIRCLE,10,(0,0))
l = Line()
l.addStation(s)
l.addStation(Station(StationShape.TRIANGLE,10,(10,10)))
l.addStation(Station(StationShape.TRIANGLE,10,(10,10)))
l.addStation(Station(StationShape.TRIANGLE,10,(10,10)))
l.addStation(Station(StationShape.TRIANGLE,10,(10,10)))
l.addStation(Station(StationShape.TRIANGLE,10,(10,10)))
print(l.stations)

t = Train(l)
p = Passenger(s,StationShape.SQUARE)
s.addLine(Line())
s.addLine(Line())
s.addToQueue(p)
print(t.line.stations[t.station])

for i in range(10):
    print(t.nextStation().id)


print(l.hasShape(StationShape.CIRCLE))
print(S_station_bias.keys(), S_station_bias.values())
print(s.generatePassenger())
showAllUUID()
countObj()
