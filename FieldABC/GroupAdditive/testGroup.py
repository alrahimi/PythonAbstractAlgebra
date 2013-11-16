from GroupModP import *
    
def test(modulus):
    print("test Group with modulus=",modulus)
    GroupModP.modulus=modulus
    r1 = GroupModP(21)
    r2 = GroupModP(22)
    r3 = GroupModP(23)
    
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



def main():
    test(5)
    test(3)
    
    
if __name__ == "__main__":
    main()
    
