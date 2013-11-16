from .Semigroup import *

#for local testing
#from Semigroup import *

class Monoid(Semigroup):
    def __init__(self,value):
        super().__init__(value)
                
    @abstractmethod  
    def getzero(self):
        pass 
	
    

