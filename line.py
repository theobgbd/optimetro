############################
# Lines
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
############################

from uuid import uuid4
import station
import passenger

# List of all lines with their object
L_lines_uuid = {}


class Line():

    def __init__(self):
        self.id = uuid.uuid4().hex
        self.types = []
        self.stations = []
        self.nbstations = 0

        L_lines_uuid[self.id] = self

    def addStation(self, station):
        if station not in S_stations_uuid:
            raise ValueError("Station "+str(station)+" doesn't exist!")
        self.stations.append(station)
        self.nbstations+=1
    
    def delStation(self, station):
        self.stations.remove(station)
        self.nbstations+=-1

   def hasShape(self, shape):
       if not isinstance(shape, StationShape):
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
