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
    
        self.line = line
        self.id = uuid4().hex

        interface.T_trains_uuid[self.id] = self
