from SemigroupMod5 import *

 
def main():
        
    r1 = SemigroupMod5(21)
    r2 = SemigroupMod5(22)
    r3 = SemigroupMod5(23)



    #use our __str__ function
    print ("r1: ", r1)
    print ("r2: ", r2)

    r = r1*r2
    print (r1, " * ", r2, " = ", r)
    r = r1*r2*r3
    print (r1, " * ", r2," * ", r3, " = ", r)

if __name__ == "__main__":
    main()
    
