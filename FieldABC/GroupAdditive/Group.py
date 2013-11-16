from .Monoid import *

#for local testing
#from Monoid import *

class Group(Monoid):
    
    def __init__(self,value):
        super().__init__(value)
        
    @abstractmethod
    def neg(self ,value):
        pass
    
    def __neg__(self):
        return self.neg(self)

    def __sub__(self,y):
        print("Group sub ,y=",y,"type(y)=",type(y))
        yneg=self.neg(y)
        return super().__add__(yneg)
  
	
    

