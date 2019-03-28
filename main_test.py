###########################################
# OptiMetro : a simple MiniMetro optimiser
# Théo Beigbeder - 2019
# Pierre Boisselier - 2019
##########################################


from interface import * 


s = Station(StationShape.CIRCLE,10,(0,0))
l = Line()
t = Train(l.id)
p = Passenger(s.id,StationShape.SQUARE)
s.addLine(Line().id)
s.addLine(Line().id)
s.addPassenger(p.id)
print(l.hasShape(StationShape.CIRCLE))

for i in s.lines:
    print(i)
