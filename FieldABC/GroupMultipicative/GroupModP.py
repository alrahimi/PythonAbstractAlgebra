from Group import *

class GroupModP(Group):
    modulus=None
    def __init__(self,value):
        super().__init__(value)
            
    def mulop(self,rhs):
        print("GroupModP mulop: type(self),type(rhs)=",type(self),type(rhs))
        #print("GroupModP mulop: type(rhs.v)=",type(rhs.v))
        s=(self.v*rhs.v) %self.modulus
        r = GroupModP(s)
        return r
    

    #optimize this by using computed field pattern from pycookbook
    def getunit(self):
        return GroupModP(1)

    def inverse(self ,value):
        y=value.v %self.modulus
        #TODO: account for y<0
        if y <2:
            z=y
        else:
            z= ((y**(self.modulus-2))%self.modulus)
        return GroupModP(z)
      
    def __str__(self):			
        s = "%s" % (self.v)
        #print "in GroupModP __str__ s=",s
        return s
    

