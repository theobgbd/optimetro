 ############################
 # I like trains
 # Pierre Boisselier - 2019
 # Theo Beigbeder - 2019
 ############################

import line
import station
import passenger

# List of all trains with their UUID
T_trains_uuid = {}

 class Train():
     
     def __init__(self, line):
         if line not in L_lines_uuid:
             raise ValueError("Line must be an existing line UUID!")
    
         self.line = line
         self.id = uuid.uuid4().hex

         T_trains_uuid[id] = self
