

class Aircraft:
    def __init__(self, make, code, type, flight_range):
        self.make = make 
        self.code = code
        self.type = type 
        self.flight_range = float(flight_range) 

    def get_make(self):
        return self.make 
    
    def __repr__(self):
        return f'Aircraft make: {self.make} code: {self.code} type: {self.type} flight range: {self.flight_range}'
    
    