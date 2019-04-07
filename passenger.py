#############################
# Passenger
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################


# Passenger will be a passive entity, the train is supposed to handle them and get them to the destination
# Please refer to Train where it's explicated

from uuid import uuid4
from enum import IntEnum
import interface


# Status of passengers
class PassengerFlag(IntEnum):
    DEAD       = 0
    WAITING    = 1
    TRAVELLING = 2

# Travel status of passengers
class PassengerTravelFlag(IntEnum):
    UNDEFINED  = 0
    DIRECT     = 1
    CONNECTION = 2


class Passenger():

    # Constructor
    def __init__(self, source, dest):
        # Check whether the destination is valid shape
        if not isinstance(dest, interface.StationShape):
            raise TypeError("Destination must be a valid shape!")
        # Check whether the source is a valid station
        if not isinstance(source, interface.Station):
            raise ValueError("Source must be an existing station!")

        # Generate an uuid for the passenger
        self.id = uuid4().hex
        # Assign its source
        self.source = source
        # Assign its destination
        self.dest = dest
        # When spawned, a passenger is waiting at the source station
        self.status = PassengerFlag.WAITING
        # Determine whether it will be a direct travel or one with connections
        self.travel = PassengerTravelFlag.CONNECTION
        for l in source.lines:
            if l.hasShape(dest):
                self.travel = PassengerTravelFlag.DIRECT        
        # The passenger spawns in a station not a train
        self.train = None
        self.station = source
        # List of stations the passenger followed to arrive  
        self.path = [source]
        
        # Tries to do something viable...
        self.line = None
        self.target_station = None
        self.follow = [source]
        self.blacklist = []

        # Assign itself to the list of passengers 
        interface.P_passengers_uuid[self.id] = self
        # Assign itself toe the list of alived passengers  
        interface.P_passengers_alive.append(self)

        #self.checkTravel()

    # Assign a train, called when a train is boarding a passenger
    def assignTrain(self, train):
        if not isinstance(train, interface.Train):
            raise TypeError("Please provide a train!")
        self.train = train
        self.status = PassengerFlag.TRAVELLING
        self.station.removeFromQueue(self)
        self.station = None
        

    # Assign a station, called when a train is unboarding a passenger 
    def assignStation(self, station):
        if not isinstance(station, interface.Station):
            raise TypeError("Please provide a station!")
        
        self.station = station
        self.train = None
        self.path.append(station)
        self.status = PassengerFlag.WAITING 

    # Self explanatory.
    # In all fairness, we still keep the passenger for future analysis, which is hard on RAM
    def kill(self, station):
        self.station = station
        self.path.append(station)
        self.status = PassengerFlag.DEAD
        self.travel = PassengerTravelFlag.UNDEFINED
        interface.P_passengers_dead.append(self)
        interface.P_passengers_alive.remove(self)
        self.train = None
        self.station.arrived.append(self)

#################################################################################
# Because the passenger should be a passive entity, those shouldn't be there...
#################################################################################    
'''
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

'''