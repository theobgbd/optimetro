 ############################
 # I like trains
 # Pierre Boisselier - 2019
 # Theo Beigbeder - 2019
 ############################

# HOW IT SHOULD WORK
# The train should be the one handling passengers.
# It must decide if it boards a specific passenger or not.
# Thus, it is responsible for finding out whether the passenger destination
# is on the line or somewhere else. If the latter case, it must find where 
# to drop the passenger allowing another train from another line to take it.

from uuid import uuid4
import interface

class Train():

    # Constructor
    def __init__(self, line):
        # A train should always be assigned to a line 
        if not isinstance(line, interface.Line):
            raise TypeError("Please provide a line.")

        # Generate the UUID of the train
        self.id = uuid4().hex
        # Assign a line to itself
        self.line = line
        # Default capacity of the train 
        self.capacity = interface.T_train_capacity
        # List of all passengers the train currently has
        self.passengers = []
        # Index of the current station
        self.station = 0    
        # Is the train going reverse ? 
        self.reverse = False
        # Assign itself to the list of trains for the whole program
        interface.T_trains_uuid[self.id] = self
        interface.T_trains.append(self)
    
    # Move the train at a speed, must be called for every train at each tick
    # TODO: Should call nextStation() when it traveled the distance
    def move(self, speed):
        return

    # Decide which passengers from the train should get out
    # Called when arriving at a station
    def unboardPassengers(self, station):
        if not isinstance(station, interface.Station):
            raise ValueError("Please provide a station!")
        
        for p in self.passengers:
            # Check first if the passenger is arrived
            if (p.dest==station.shape):
                self.passengers.remove(p)
                p.kill(station)

            # Does the station has enough capacity?
            # We allow + 1 to the capacity to allow "swaps" to happen
            elif len(station.queue)>station.capacity:
                return    

            # If the station has more than one line we can check connections
            # And if the passenger is in a connection travel
            elif (len(station.lines)>1) and (p.travel==interface.PassengerTravelFlag.CONNECTION):
                # We want to know if there is a path to the destination
                connection = self.line.isConnected(p.dest, station.lines)
                # If there is indeed a path we unboard the passenger
                # TODO: There can be a problem if there are more than 3 lines to connect!!!
                # TODO: Find a way to fix this
                if connection != False:                
                    self.passengers.remove(p)
                    p.assignStation(station)
                    
                
    # Decide which passengers in the station to board
    # Called after unboardPassengers when arriving at a station
    def boardPassengers(self, station):
        if not isinstance(station, interface.Station):
            raise ValueError("Please provide a station!")

        for p in station.queue:
            # We first check if we have enough capacity to board a passenger
            if len(self.passengers)>=self.capacity:
                return
            # We then check if there is indeed the destination in our line
            elif self.line.hasShape(p.dest):
                p.assignTrain(self)
                self.passengers.append(p)
            # Otherwise we check if it's a connection travel
            elif p.travel==interface.PassengerTravelFlag.CONNECTION:   
                connection = self.line.isConnected(p.dest,station.lines)
                if connection != False:
                    p.assignTrain(self)
                    self.passengers.append(p)


    # Enter a new station and manage passengers
    def nextStation(self):
        # Change the index to the new station
        if self.station == len(self.line.stations)-1:
            self.reverse = True
        elif self.station == 0:
            self.reverse = False

        if self.reverse:
            self.station+=-1
        else:
            self.station+=1

        new_station = self.line.stations[self.station]

        # Assign the new station to all passengers
        for p in self.passengers:
            p.station=new_station

        # Unboard all passengers
        self.unboardPassengers(new_station)
        # Board passengers at the current station
        self.boardPassengers(new_station)

############
# DEPRECATED
############
    # Adds a passenger to the train
    def addPassenger(self, passenger):
        self.nextStation()

    # Remove a passenger from the train
    def removePassenger(self, passenger):
        self.nextStation()
        
