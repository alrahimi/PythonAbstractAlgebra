from Monoid import *

class MonoidModP(Monoid):
    modulus=None
    def __init__(self,value):
        super().__init__(value)
            
    def addop(self,rhs):
        print("MonoidModP addop: type(self),type(rhs)=",type(self),type(rhs))
        s=(self.v+rhs.v) %self.modulus
        r = MonoidModP(s)
        return r
    

    #optimize this by using computed field pattern from pycookbook
    def getzero(self):
        return MonoidModP(0)
     
    def __str__(self):			
        s = "%s" % (self.v)
        #print "in MonoidModP __str__ s=",s
        return s
    

