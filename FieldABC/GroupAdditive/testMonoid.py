from MonoidModP import *


def main():

    MonoidModP.modulus=5
    r1 = MonoidModP(21)
    r2 = MonoidModP(22)
    r3 = MonoidModP(23)



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
    
