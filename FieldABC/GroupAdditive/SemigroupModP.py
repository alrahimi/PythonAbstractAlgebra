from Semigroup import *

class SemigroupModP(Semigroup):
    modulus=None
    def __init__(self,value):
        super().__init__(value)
            
    def addop(self,rhs):
        print("SemigroupModP addop: type(self),type(rhs)=",type(self),type(rhs))
        s=(self.v+rhs.v) %self.modulus
        r = SemigroupModP(s)
        return r
       
    def __str__(self):			
        s = "%s" % (self.v)
        #print "in SemigroupModP __str__ s=",s
        return s
    

