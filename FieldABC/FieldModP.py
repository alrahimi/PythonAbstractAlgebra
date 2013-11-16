from Field import *

class FieldModP(Field):
    #modulus=None
    def __init__(self,value,modulus):
        super().__init__(value)
        self.modulus=modulus
            
    def addop(self,rhs):
        print("FieldModP addop: type(self),type(rhs)=",type(self),type(rhs))
        s=(self.v+rhs.v) %self.modulus
        r = FieldModP(s,self.modulus)
        return r
    

    #optimize this by using computed field pattern from pycookbook
    def getzero(self):
        return FieldModP(0,self.modulus)

    def neg(self ,value):
        return FieldModP(self.modulus-(value.v %self.modulus),self.modulus)
      
    def __str__(self):			
        s = "%s" % (self.v)
        #print "in FieldModP __str__ s=",s
        return s
            
    def mulop(self,rhs):
        print("FieldModP mulop: type(self),type(rhs)=",type(self),type(rhs))
        #print("FieldModP mulop: type(rhs.v)=",type(rhs.v))
        s=(self.v*rhs.v) %self.modulus
        r = FieldModP(s,self.modulus)
        return r
    

    #optimize this by using computed field pattern from pycookbook
    def getunit(self):
        return FieldModP(1,self.modulus)

    def inverse(self ,value):
        y=value.v %self.modulus
        #TODO: account for y<0
        if y <2:
            z=y
        else:
            z= ((y**(self.modulus-2))%self.modulus)
        return FieldModP(z,self.modulus)
    

