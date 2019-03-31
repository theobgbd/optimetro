#############################
# Interface
# List of global variables
# #Fortran représente
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################
# Comments:
# Yes, it's 1977 again, we old and cool
# - P


# Imports

from station import *
from line import *
from passenger import *
from train import *




##########
# Station
##########

# Dictionnary associating each uuid to its station object
S_stations_uuid = {}
# Dictionnary associating each station coordinates to its uuid (coord:uuid), useful for OpenCV
S_stations_coord = {}
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

# Max capacity of passengers, including queue ?
S_stations_capacity = 10

##########
# Passengers
##########

# List of all passenger uuid with their object
P_passengers_uuid = {}

# List of all passengers currently alive
P_passengers_alive = []

# List of passengers that have done their travel, keeping them for analytics
P_passengers_dead = []

##########
# Lines
##########

# List of all lines with their object
L_lines_uuid = {}

##########
# Trains
##########

# List of all trains with their UUID
T_trains_uuid = {}

# Default capacity of a train
T_train_capacity = 10

###################################
# Some useful functions for debug
###################################

# Show every obj UUID in the program
# Use to be determined, I was bored. - P
def showAllUUID():
    print("-= List of objects =-")
    for i in S_stations_uuid:
        print("Station: "+i)
    for i in L_lines_uuid:
        print("Line: "+i)
    for i in T_trains_uuid:
        print("Train: "+i)
    for i in P_passengers_uuid:
        print("Passenger: "+i)


# Show how many objects there are
def countObj():
    print("-= Object count =-")
    print("Stations: "+str(S_stations_uuid.__len__()))
    print("Lines: "+str(L_lines_uuid.__len__()))
    print("Trains: "+str(T_trains_uuid.__len__()))
    print("Passengers: "+str(P_passengers_uuid.__len__()))
    print("\tAlive: "+str(P_passengers_alive.__len__()))
    print("\tDead: "+str(P_passengers_dead.__len__()))

# Markers table for Matlplotlib plot
switch_mark = {
    1: "o",
    2: "^",
    3: "s",
    4: "P",
    5: "1",
    6: "v",
    7: "*",
    8: "p",
    9: "D",
    10: "d",
}
