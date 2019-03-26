#############################
# Passenger
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################

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
        if not isinstance(dest, StationShape): 
            raise TypeError("Destination must be a valid shape!")
        if source not in S_stations_uuid:
            raise ValueError("Source must be an existing station!")

        self.id = uuid.uuid4().hex
        self.source = source 
        self.dest = dest
        self.status = PassengerFlag.WAITING
        self.travel = PassengerTravelFlag.UNDEFINED # Todo.

        P_passengers_uuid[self.id] = self
        P_passengers_alive.append(self.id)

    # Not a stupid set, figure itself whether the station is a connection or a direct
    def setTravelFlag(self):
        return

