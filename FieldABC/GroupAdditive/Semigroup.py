
from abc import ABCMeta, abstractmethod

class Semigroup(metaclass=ABCMeta):

    @abstractmethod
    def addop(self,x):
        pass
    
    def __init__(self,value):
        self.v=value
                
    def __add__(self,rhs):
        print("SemigroupAdd rhs=",rhs,"type(rhs)=",type(rhs))
        #r = Semigroup(self.addop(rhs))    
        #return r
        return self.addop(rhs)
    
    def __str__(self):          
        s = "%s" % (self.v)
        return s
        
