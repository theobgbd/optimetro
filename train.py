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
        self.capacity = interface.T_train_capacity
        self.passengers = []
        self.station = 0    # Holds the index of the station
        self.reverse = False
        interface.T_trains_uuid[self.id] = self
        interface.T_trains.append(self)

    def addPassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a passenger!")
        self.passengers.append(passenger)
        passenger.assignTrain(self)

    def removePassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a passenger!")
        self.passengers.remove(passenger)
        passenger.assignStation(self.line.stations[self.station])
        #########passenger.updateTravel(self.line.stations[self.station])

    # TODO: Make a function moving the train, distance between 2 stations and speed
    # Speed in ticks ofc
    def move(self, spped):
        return

    def connection(self):
        for p in self.line.stations[self.station].queue:
            print(p)
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
        for i in self.passengers:
            i.station=self.line.stations[self.station]
            #i.assignStation(self.line.stations[self.station])
        return self.line.stations[self.station]
