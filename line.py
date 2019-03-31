############################
# Lines
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
############################

from uuid import uuid4
import interface



class Line():

    def __init__(self):
        self.id = uuid4().hex
        self.types = []
        self.stations = []
        self.nbstations = 0

        interface.L_lines_uuid[self.id] = self

    def addStation(self, station):
        if not isinstance(station, interface.Station):
            raise TypeError("Please provide a station!")
        self.stations.append(station)
        self.types.append(station.shape)
        self.nbstations+=1
    
    def delStation(self, station):
        self.stations.remove(station)
        self.nbstations+=-1

    def hasShape(self, shape):
        if not isinstance(shape, interface.StationShape):
            raise TypeError("Please provide a valid station shape!") 
        for i in self.types:
            if shape == i:
                return True
        return False
    
    def hasStation(self, station):
        for i in self.stations:
            if i == station:
                return True
        return False

    # Get the next station in the line
    # DEPRECATED, train is handling the next station
    def nextStation(self, station):
       if station == self.stations[len(self.stations)-1]:
           return self.stations[-1]
       return self.stations[self.stations.index(station)+1]
       
        



'''
#!/usr/bin/python
# Line class 
import station
class Line:
    self.stations = list() # Stations IDs
    self.trains   = list() # Trains IDs
    self.color    = default_color
    self.lines = [StationShape.CIRCLE, StationShape.CHTULU]
    
    def __init__(self, color):
        self.color = color

    def addStation(new_station, target_station) :
        self.stations_list = append(new_station)
        
    def removeStation(old_station) :
        self.station_list = remove(old_station)

    def reorderStations() :
        self.stations = shuffle()
        
    def isInLine(self, shape):
        if not isinstance(shape, StationShape):
            raise ValueError("The shape provided is not valid!")
        
    def addTrain() :
   ''' 
