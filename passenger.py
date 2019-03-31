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
        self.line = None

        interface.P_passengers_uuid[self.id] = self
        interface.P_passengers_alive.append(self)

    # Not a stupid set, figure itself whether the station is a connection or a direct
    def setTravelFlag(self):
        if self.line
        return
    
    '''
    # To be run each time a train is entering a station
    def checkTravel(self, station):
        if not isinstance(station, interface.Station):
            raise TypeError("Please provide a valid station!")

        self.path.append(station)
        if station.shape == self.dest:
            self.kill()
            return
        
        nextLine(station)
    
    '''
    



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
        

    def kill(self):
        self.status = PassengerFlag.DEAD
        self.travel = PassengerTravelFlag.UNDEFINED
        interface.P_passengers_dead.append(self)
        interface.P_passengers_alive.remove(self)
        self.train = None
        self.station.arrived.append(self)


    