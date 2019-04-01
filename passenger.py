#############################
# Passenger
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################


# Passenger will be a passive entity, the train is supposed to handle them and get them to the destination

from uuid import uuid4
from enum import IntEnum
import interface


class PassengerFlag(IntEnum):
    DEAD = 0
    WAITING = 1
    TRAVELLING = 2

class PassengerTravelFlag(IntEnum):
    UNDEFINED = 0
    DIRECT = 1
    CONNECTION = 2



class Passenger():


    def __init__(self, source, dest):
        if not isinstance(dest, interface.StationShape):
            raise TypeError("Destination must be a valid shape!")
        if not isinstance(source, interface.Station):
            raise ValueError("Source must be an existing station!")

        self.id = uuid4().hex
        self.source = source
        self.dest = dest
        self.status = PassengerFlag.WAITING
        self.travel = PassengerTravelFlag.UNDEFINED # Todo.
        self.train = None
        self.station = source
        self.path = [source]
        self.follow = [source]
        self.line = None

        interface.P_passengers_uuid[self.id] = self
        interface.P_passengers_alive.append(self)

        self.checkTravel()

    # Not a stupid set, figure itself whether the station is a connection or a direct
    def setTravelFlag(self):
        return


    def checkTravel(self):
        
        # Check whether it will be a direct travel
        for i in self.source.lines:
            if i.hasShape(self.dest):
                self.travel = PassengerTravelFlag.DIRECT
                return
        # This is going to be tricky
        self.travel = PassengerTravelFlag.CONNECTION
        if self.findPath():
            print("Follow stations: ",self.follow)
        else:
            print("No path to station!")
        
    
    def findPath(self):
        for i in self.source.lines:
            tmp = i.isConnected(self.dest,interface.L_lines,self.follow)
            if tmp != False:
                self.follow = tmp
                return True
        return False
    
    def next(self):
        if len(self.follow)>1:
            return self.follow[1]
        return self.follow[0]


  

    def assignTrain(self, train):
        if not isinstance(train, interface.Train):
            raise TypeError("Please provide a train!")
        self.train = train
        self.travel = PassengerFlag.TRAVELLING
        self.station = None

    def assignStation(self, station):
        if not isinstance(station, interface.Station):
            raise TypeError("Please provide a station!")
        self.station = station
        self.train = None
        self.path.append(station)
        if station.shape == self.dest:
            self.kill()
        self.checkTravel()


    def kill(self):
        self.status = PassengerFlag.DEAD
        self.travel = PassengerTravelFlag.UNDEFINED
        interface.P_passengers_dead.append(self)
        interface.P_passengers_alive.remove(self)
        self.train = None
        self.station.arrived.append(self)
