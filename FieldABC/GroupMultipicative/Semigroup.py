
from abc import ABCMeta, abstractmethod

class Semigroup(metaclass=ABCMeta):

    @abstractmethod
    def mulop(self,x):
        pass
    
    def __init__(self,value):
        self.v=value
                
    def __mul__(self,rhs):
        print("SemigroupMul rhs=",rhs,"type(rhs)=",type(rhs))
        #r = Semigroup(self.mulop(rhs))    
        #return r
        return self.mulop(rhs)
    
    def __str__(self):          
        s = "%s" % (self.v)
        return s
        
