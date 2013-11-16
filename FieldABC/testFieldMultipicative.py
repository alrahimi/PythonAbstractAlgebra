from FieldModP import *
    
def test(modulus):
    print("test Group with modulus=",modulus)
    FieldModP.modulus=modulus
    r1 = FieldModP(21)
    r2 = FieldModP(22)
    r3 = FieldModP(23)
    
    #use our __str__ function
    print ("r1: ", r1)
    print ("r2: ", r2)

    r = r1*r2
    print (r1, " * ", r2, " = ", r)
    r = r1*r2*r3
    print (r1, " * ", r2," * ", r3, " = ", r)

    unit=r2.getunit()
    print ("type(unit)=",type(unit),"unit=",unit)
    r1=r1*unit
    print ("r1*unit=",r1)

    r2inverse=r2.inverse(r2)
    
    print ("r2 inverse=",r2inverse)
    #print("r1inverse type=",type(r1inverse))

    
    r2inverse=unit/r2
    print ("unit/r2=",r2inverse)
       
    
    r=r1/r2
    
    #r=r1*r1inverse
    
    print ("r1/r2=",r1,"/",r2,"=",r)
    print("End of test Group with modulus=",modulus)



def main():
    test(5)
    test(3)
   
    
    
if __name__ == "__main__":
    main()
    
