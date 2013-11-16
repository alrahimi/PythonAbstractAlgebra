from Semigroup import *

class SemigroupStrings(Semigroup):
    def __init__(self,value):
        self.v=value
            
    def addop(self,x,y):
        r = SemigroupStrings(self.v+rhs.v)
        return r
      
    def __str__(self):			
        s = "%s" % (self.v)
        #print "in SemigroupStrings __str__ s=",s
        return s
    

