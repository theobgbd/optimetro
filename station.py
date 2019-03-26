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
import passenger
import line
from enum import IntEnum




# List of stations with their ID 
# DEPRECATED
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

class StationShape(IntEnum):
    CIRCLE = 1
    TRIANGLE = 2
    SQUARE = 3
    CROSS = 4
    DIAMOND = 5
    PIZZA = 6
    STAR = 7
    PENTAGON = 8
    RHOMBUS = 9
    LEAF = 10

# Dictionnary associating each uuid to its station object
S_stations_uuid = {} 
# Dictionnary associating each station coordinates to its uuid (coord:uuid), useful for OpenCV 
S_stations_coord = {}
# List of bias for each type of station
S_station_bias = {
    1:1,
    2:10,
    3:30,
    4:100,
    5:100,
    6:100,
    7:100,
    8:100,
    9:100,
    10:100
}

class Station:
    
    def __init__(self, shape, bias, coord):
       # if shape not in S_station_shapes:
       #     raise ValueError(str(shape)+" is not a valid shape!") 
        if not isinstance(shape, StationShape):
            raise ValueError("Shape must be a valid one from StationShape!")
        if not isinstance(coord, tuple):
            raise ValueError("Coordinates must be a tuple!")

        self.shape = shape 
        self.id = uuid.uuid4().hex 
        self.bias = bias
        self.coord = coord 
        self.queue = []
        self.lines = []

        S_stations_uuid[self.id] = self
        S_stations_coord[self.coord] = self.id

    # Must be called by Line when adding a station to it
    def addLine(self, line):
        if line not in L_lines_uuid:
            raise ValueError("This line doesn't exist!")
        self.lines.append(line)

    # Must be called when adding a passenger to the queue
    def addPassenger(self, passenger):
        if passenger not in P_passengers_alive:
             raise ValueError("This passenger doesn't exist, or is dead!")
        self.queue.append(passenger)

    # Must be called when a passenger is leaving the station
    def removePassenger(self, passenger):
        if passenger not in P_passengers_alive:
            raise ValueError("This passenger doesn't exist, or is dead!")
        self.queue.remove(passenger)

    
    

s = Station(StationShape.CIRCLE,1,(1,1))

'''
for i in range(1,11):
    Station(i,S_station_bias[i],(random.randint(0,512),random.randint(0,512)))

for i in S_stations_coord:
    print("Coord : "+str(i)+", UUID : "+str(S_stations_uuid[S_stations_coord[i]].id))
'''
