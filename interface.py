#############################
# Interface
# List of global variables
# #Fortran représente
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################


# Imports 

import station
import line
import passenger
import train


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