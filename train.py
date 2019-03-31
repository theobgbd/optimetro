 ############################
 # I like trains
 # Pierre Boisselier - 2019
 # Theo Beigbeder - 2019
 ############################


from uuid import uuid4
import interface

class Train():

    def __init__(self, line):
        if not isinstance(line, interface.Line):
            raise TypeError("Please provide a line.")

        self.id = uuid4().hex
        self.line = line
        self.capacity = 10
        self.passengers = []
        interface.T_trains_uuid[self.id] = self
        self.station = 0    # Holds the index of the station
        self.reverse = False

    def addPassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a passenger!")
        self.passengers.append(passenger)
        passenger.assignTrain(self)

    def removePassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a passenger!")
        self.passengers.remove(passenger)
        passenger.kill()

    # TODO: Make a function moving the train, distance between 2 stations and speed
    # Speed in ticks ofc
    def move(self, spped):
        return

    def connection(self):
        return
        # TODO: just do it.

    # Return the next station
    def nextStation(self):
        if self.station == len(self.line.stations)-1:
            self.reverse = True
        elif self.station == 0:
            self.reverse = False
        if self.reverse:
            self.station+=-1
            return self.line.stations[self.station]
        self.station+=1
        return self.line.stations[self.station]
