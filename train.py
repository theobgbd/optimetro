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
            raise TypeError("Please provide a line!")
        
        self.id = uuid4().hex   
        self.line = line # Line assigned
        self.capacity = T_train_capacity  # Capacity of the train
        self.passengers = [] # List of all passengers on board
        self.station = 0    # Holds the index of the station
        self.reverse = False
        interface.T_trains_uuid[self.id] = self

    def addPassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a passenger!")
        passengers.append(passenger) 
        passenger.assignTrain(self)

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


