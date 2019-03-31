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
        self.arrived = []

        interface.S_stations_uuid[self.id] = self
        interface.S_stations_coord[self.coord] = self.id
        

    # Must be called by Line when adding a station to it
    def addLine(self, line):
        if not isinstance(line, interface.Line):
            raise TypeError("Provide a valid line!")
        self.lines.append(line)

    def removeLine(self, line):
        # Already raise a ValueError if line not in lines
        self.lines.remove(line)
    
    # Generate a passenger and add it to the queue
    def generatePassenger(self):
        # generate random number 1-10 with propability relative to bias
        tmp = random.choices(range(1,11), interface.P_passengers_probabilities)
        tmp = interface.Passenger(self,StationShape(tmp[0]))
        self.addToQueue(tmp)
        return tmp

    # Must be called when adding a passenger to the queue
    def addToQueue(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a Passenger!")
        if passenger.status == interface.PassengerFlag.DEAD:
            raise ValueError("This passenger is dead!") 
        passenger.status = interface.PassengerFlag.WAITING
        self.queue.append(passenger)

    # Must be called when a passenger is leaving the station
    def removeFromQueue(self, passenger):
        # Already raise a ValueError if passenger is not in the queue
        self.queue.remove(passenger)

    
  
