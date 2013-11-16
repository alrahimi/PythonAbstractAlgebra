from FieldModP import *

class FieldMod3(FieldModP):
    def __init__(self,value,modulus=3):
        super().__init__(value,modulus)
    
class FieldMod5(FieldModP):
    def __init__(self,value,modulus=5):
        super().__init__(value,modulus)
        

createFieldModP = {
    3 : FieldMod3,
    5 : FieldMod5,

}    
def test(modulus):
    print("test Group with modulus=",modulus)
    r1 = createFieldModP[modulus](21)
    r2 = createFieldModP[modulus](22)
    r3 = createFieldModP[modulus](23)
    
    #use our __str__ function
    print ("r1: ", r1)
    print ("r2: ", r2)

    r = r1+r2
    print (r1, " + ", r2, " = ", r)
    r = r1+r2+r3
    print (r1, " + ", r2," + ", r3, " = ", r)

    r=r+r.getzero()
    print ("r+zero=",r)

    r2neg=r2.neg(r2)
    
    print ("r2 neg=",r2neg)
    #print("r1neg type=",type(r1neg))

    r2neg=-r2
    print ("-r2=",r2neg)
       
    
    r=r1-r2
    
    #r=r1+r1neg
    
    print ("r1-r2=",r1,"-",r2,"=",r)
    print("End of test Group with modulus=",modulus)

def testMixedModulus(modulus1,modulus2):
    print("test Group with modulus=",modulus1,modulus2)
    r1 = createFieldModP[modulus1](21)
    r2 = createFieldModP[modulus1](22)
    r3 = createFieldModP[modulus1](23)

    s1 = createFieldModP[modulus2](21)
    s2 = createFieldModP[modulus2](22)
    s3 = createFieldModP[modulus2](23)

    print("test Group with modulus=",modulus1)
    print ("r1: ", r1)
    print ("r2: ", r2)

    r = r1+r2
    print (r1, " + ", r2, " = ", r)

    
    print("test Group with modulus=",modulus2)
    print ("s1: ", s1)
    print ("s2: ", s2)

    s = s1+s2
    print (s1, " + ", s2, " = ", s)
    
def main():
    test(5)
    test(3)

    testMixedModulus(3,5)

    
if __name__ == "__main__":
    main()
    
