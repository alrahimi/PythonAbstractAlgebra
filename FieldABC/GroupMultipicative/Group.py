from .Monoid import *

#for local testing
#from Monoid import *

class Group(Monoid):
    
    def __init__(self,value):
        super().__init__(value)
        
    @abstractmethod
    def inverse(self ,value):
        pass
 
    def __truediv__(self,y):
        print("Group div ,y=",y,"type(y)=",type(y))
        yinverse=self.inverse(y)
        return super().__mul__(yinverse)
  
	
    

