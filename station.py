###########################
# Stations
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
###########################


import random
import uuid
from enum import IntEnum
import interface

# List of all possible shapes
class StationShape(IntEnum):
    UNDEFINED   = 0
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

    # Constructor
    def __init__(self, shape, bias, coord):
        # A station needs a shape to exist
        if not isinstance(shape, StationShape):
            raise TypeError("Shape must be a valid one from StationShape!")
        # A station should have a location
        if not isinstance(coord, tuple):
            raise TypeError("Coordinates must be a tuple!")

        # Generate an uuid for the station
        self.id = uuid.uuid4().hex
        # Assign its shape
        self.shape = shape
        # Assign its bias
        self.bias = bias
        # Assign a location to id
        self.coord = coord
        # Initialize the passenger queue
        self.queue = []
        # Lines connected to the station
        self.lines = []
        # Queue capacity
        self.capacity = interface.S_stations_capacity
        # List of all passengers that ended their travel at this station
        self.arrived = []

        self.vertex = interface.Network.add_vertex()

        interface.S_stations_uuid[self.id] = self
        interface.S_stations_coord[self.coord] = self.id
        interface.S_stations.append(self)

    # Adds a line to the list of lines after checking if it's a valid line
    # Must be called by Line when adding a station to it
    def addLine(self, line):
        if not isinstance(line, interface.Line):
            raise TypeError("Provide a valid line!")
        self.lines.append(line)

    # Removes a line from the list
    # Exists for symetry with addLine()
    def removeLine(self, line):
        # Already raise a ValueError if line not in lines
        self.lines.remove(line)

    # Generate a passenger and adds it to the queue
    def generatePassenger(self,limit):
        # generate a random number from 1 to 10 with propability relative to bias
        a = random.choices(range(1,limit), interface.P_passengers_probabilities[1:limit])
        if (StationShape(a[0]) != self.shape) :
            tmp = interface.Passenger(self,StationShape(a[0]))
            self.addToQueue(tmp)
            return StationShape(a[0])
        return 0

    # Adds a passenger to the queue
    # Must be called when adding a passenger to the queue
    def addToQueue(self, passenger, suppressCapacity=False):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a Passenger!")
        if passenger.status == interface.PassengerFlag.DEAD:
            raise ValueError("This passenger is dead!")

        if len(self.queue)>self.capacity and not suppressCapacity:
            raise ValueError("STATION "+self.id+" REACHED FULL CAPACITY")

        self.queue.append(passenger)

    # Removes a passenger from the queue
    # Must be called when a passenger is leaving the station
    def removeFromQueue(self, passenger):
        # Already raise a ValueError if passenger is not in the queue
        self.queue.remove(passenger)
