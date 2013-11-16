from FieldModP import *

class FieldMod7(FieldModP):
    def __init__(self,value,modulus=3):
        super().__init__(value,modulus)
    
class FieldMod11(FieldModP):
    def __init__(self,value,modulus=11):
        super().__init__(value,modulus)
        
createFieldModP = {
    7 : FieldMod7,
    11 : FieldMod11,

} 
def test(modulus):
    print("test Group with modulus=",modulus)
    r1 = createFieldModP[modulus](21)
    r2 = createFieldModP[modulus](22)
    r3 = createFieldModP[modulus](24)

    #verify iheriting from two semigroups with a 'v' member doesnt duplicate v
    print("\nprint r1 dic:")
    print("r1.__dict__=",r1.__dict__)
    print("End  r1 dic.Proves there is only one 'v'\n")
    
    
    #use our __str__ function
    print ("r1: ", r1)
    print ("r2: ", r2)
    print ("r3: ", r3)

    r=r1*(r2+r3)
    print ("r1*(r2+r3)=",r)

    r=r1*r2+r1*r3
    print ("r1*r2+r1*r3=",r)

    
    r=(r2+r3)*r1
    print ("(r2+r3)*r1=",r)



def main():
    test(7)
    test(11)
    
    
if __name__ == "__main__":
    main()
    
