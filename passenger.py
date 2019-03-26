#############################
# Passenger
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################

from uuid import uuid4
from enum import IntEnum
import station 



# List of all passenger uuid with their object 
P_passengers_uuid = {}

# List of all passengers currently alive
P_passengers_alive = []

# List of passengers that have done their travel, keeping them for analytics 
P_passengers_dead = [] 


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
        if dest not isinstance(dest, StationShape): 
            raise ValueError("Destination must be a valid shape!")
        if source not in S_stations_uuid:
            raise ValueError("Source must be an existing station!")

        self.id = uuid.uuid4().hex
        self.source = source 
        self.dest = dest
        self.status = PassengerFlag.WAITING
        self.travel = PassengerTravelFlag.UNDEFINED

        P_passengers_uuid[self.id] = self
        P_passengers_alive.append(self.id)
