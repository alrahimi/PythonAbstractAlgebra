from MonoidMod5 import *


def main():

    
    #
    #have to call r.setzero(ZERO)
    #how to set if per class and not per instance (in monoid 5)
    #solution only have getzero as an abstract method and implement it in MonoidMod5
    
    r1 = MonoidMod5(21)
    r2 = MonoidMod5(22)
    r3 = MonoidMod5(23)



    #use our __str__ function
    print ("r1: ", r1)
    print ("r2: ", r2)

    r = r1+r2
    print (r1, " + ", r2, " = ", r)
    r = r1+r2+r3
    print (r1, " + ", r2," + ", r3, " = ", r)

    r=r+r.getzero()
    print ("r+zero=",r)
if __name__ == "__main__":
    main()
    
