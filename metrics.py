#############################
# Metrics
# Pierre Boisselier - 2019
# Theo Beigbeder - 2019
#############################
# Comments:
# “A single death is a tragedy; a million deaths is a statistic.
#  A billion is a succesful AI.”
# ― T ft. Joseph Stalin
# ^ quoting Stalin, how to not get approved for a US Visa


from uuid import uuid4
import interface

##### Metrics tables #####
global_load = []

##### Metrics Files #####
f_gload = open("train_load.txt", "w")

##### Functions #####
def getTrainsLoad(trainSet):
    load = 0
    for train in trainSet :
        load = load + len(train.passengers)/(train.capacity*len(trainSet))
    return load

def getStationsLoad(stationSet):
    load = 0
    for station in stationSet :
        load = load + len(station.queue)/(station.capacity*len(stationSet))
    return load
