###########################
# Stations
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
###########################

'''

La taille du génome, c'est le nombre de stations sur une ligne
La mutation, c'est un nouveau raccordement
Et les critères de performance, c'est la fluidité du trafic
'''

import random
import uuid
from enum import IntEnum
import interface




# List of stations with their ID 
# DEPRECATED
'''
S_station_shapes = {
    1:'Circle',
    2:'Triangle',
    3:'Square',
    4:'Cross',
    5:'Diamond',
    6:'Pizza', 
    7:'Star', 
    8:'Pentagon', 
    9:'Rhombus',
    10:'Leaf'
}
'''
class StationShape(IntEnum):
    CIRCLE      = 1
    TRIANGLE    = 2
    SQUARE      = 3
    CROSS       = 4
    DIAMOND     = 5
    PIZZA       = 6
    STAR        = 7
    PENTAGON    = 8
    RHOMBUS     = 9
    LEAF        = 10


class Station():

    def __init__(self, shape, bias, coord):
        if not isinstance(shape, StationShape):
            raise TypeError("Shape must be a valid one from StationShape!")
        if not isinstance(coord, tuple):
            raise TypeError("Coordinates must be a tuple!")

        self.shape = shape 
        self.id = uuid.uuid4().hex 
        self.bias = bias
        self.coord = coord 
        self.queue = []
        self.lines = []
        self.capacity = interface.S_stations_capacity

        interface.S_stations_uuid[self.id] = self
        interface.S_stations_coord[self.coord] = self.id
        

    # Must be called by Line when adding a station to it
    def addLine(self, line):
        '''
        if line not in interface.L_lines_uuid:
            raise ValueError("This line doesn't exist!")
        '''
        if not isinstance(line, interface.Line):
            raise TypeError("Provide a valid line!")
        self.lines.append(line)

    def removeLine(self, line):
        # Already raise a ValueError if line not in lines
        self.lines.remove(line)
    
    # Generate a passenger and add it to the queue
    def generatePassenger(self):
        # generate random number 1-10 with propability relative to bias
        return

    # Must be called when adding a passenger to the queue
    def addPassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a Passenger!")
        if passenger.status == interface.PassengerFlag.DEAD:
            raise ValueError("This passenger is dead!") 
        passenger.status = interface.PassengerFlag.WAITING
        self.queue.append(passenger)

    # Must be called when a passenger is leaving the station
    def removePassenger(self, passenger):
        # Already raise a ValueError if passenger is not in the queue
        self.queue.remove(passenger)

    
    
''''
Station(StationShape.CIRCLE,1,(1,1))
Station(StationShape.TRIANGLE,2,(0,0))
print("Len:"+str(len(S_stations_uuid)))
for i in S_stations_uuid:
    print("UUID:"+i)
    print("ID:"+S_stations_uuid[i].id)
    print("Coord:"+str(S_stations_uuid[i].coord))


for i in range(1,11):
    Station(i,S_station_bias[i],(random.randint(0,512),random.randint(0,512)))

for i in S_stations_coord:
    print("Coord : "+str(i)+", UUID : "+str(S_stations_uuid[S_stations_coord[i]].id))
'''
