###########################
# Stations
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
###########################

'''

La taille du génome, c'est le nombre de stations sur une ligne
La mutation, c'est un nouveau raccordement
Et les critères de performance, c'est la fluidité du trafic
'''

import random
import hashlib
import uuid


# List of stations with their ID
S_station_shapes = {
    1:'Circle',
    2:'Triangle',
    3:'Square',
    4:'Cross',
    5:'Diamond',
    6:'Pizza', 
    7:'Star', 
    8:'Pentagon', 
    9:'Rhombus',
    10:'Leaf'
}

# Dictionnary associating each hash to its station object
S_stations_hash = {} 
# List of bias for each type of station
S_station_bias = {
    1:1,
    2:10,
    3:30,
    4:100,
    5:100,
    6:100,
    7:100,
    8:100,
    9:100,
    10:100
}

class Station:
    
    def __init__(self, shape, bias, coord):
        if shape not in S_station_shapes:
            raise ValueError(str(shape)+" is not a valid shape!") 
        if not isinstance(coord, tuple):
            raise ValueError("Coordinates must be a tuple!")

        self.shape = shape 
        self.id = uuid.uuid4().hex 
        S_stations_hash[self.id] = self
        self.bias = bias
        self.coord = coord 


'''
for i in range(1,11):
    Station(i,S_station_bias[i],(random.randint(0,512),random.randint(0,512)))

for i in S_stations_hash.values():
    print(i.coord)
'''
