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
        self.passengers = []
        interface.T_trains_uuid[self.id] = self
        self.station = line.stations[0]

    def addPassenger(self, passenger):
        if not isinstance(passenger, interface.Passenger):
            raise TypeError("Please provide a passenger!")
        passengers.append(passenger) 
        passenger.assignTrain(self)

    def move(self, spped):
        return

    def connection(self):
        # TODO: just do it.

#        for i in self.passengers:
#            i.checkTravel(station)

