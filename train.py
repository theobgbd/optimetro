 ############################
 # I like trains
 # Pierre Boisselier - 2019
 # Theo Beigbeder - 2019
 ############################


from uuid import uuid4
import interface

class Train():
     
    def __init__(self, line):
        if line not in interface.L_lines_uuid:
            raise ValueError("Line must be an existing line UUID!")
    
        self.line = line
        self.id = uuid4().hex

        interface.T_trains_uuid[id] = self
