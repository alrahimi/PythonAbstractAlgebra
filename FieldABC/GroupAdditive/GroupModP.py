from Group import *

class GroupModP(Group):
    modulus=None
    def __init__(self,value):
        super().__init__(value)
            
    def addop(self,rhs):
        print("GroupModP addop: type(self),type(rhs)=",type(self),type(rhs))
        s=(self.v+rhs.v) %self.modulus
        r = GroupModP(s)
        return r
    

    #optimize this by using computed field pattern from pycookbook
    def getzero(self):
        return GroupModP(0)

    def neg(self ,value):
        return GroupModP(self.modulus-(value.v %self.modulus))
      
    def __str__(self):			
        s = "%s" % (self.v)
        #print "in GroupModP __str__ s=",s
        return s
    

