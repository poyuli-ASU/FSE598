from typing import final

def main():
   pet = Pet("Alf",5)
   pet.printName()
   pet.printAge()
   pet.__name = "Moon"
   pet.__age = 6
   pet._att = "Moon2"
   pet._att2 = 62
   pet.printName()
   pet.printAge()
   pet.setName("Luna")
   pet.setAge(4)
   pet.printName()
   pet.printAge()
   cat = Cat("Kitty",3)
   cat.printName()

class Pet: #parent class
    #class attribute 
    breed = "Chihuahua"
    #constructor and instance attribute
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self._att = name    
        self._att2 = age
    def setName(self, nm):
        self.__name = nm
        self._att = nm
    @final
    def printName(self):
        print("Pet name is ", self.__name)
        print("Pet att is ", self._att)
    def setAge(self, ag):
        self.__age = ag
        self._att2 = ag
    @final
    def printAge(self):
        print("Pet age is ", self.__age)
        print("Pet att2 is ", self._att2)

class Cat(Pet): #child class
    origin = "Taiwan"
    def __init__(self, name, age):
        super().__init__(name, age)
        self.__cat__ = "Persian"
    def printName(self):                
        print("Overriding the method")
        

if __name__ == "__main__":
    main()
    # Q2 : According to the M2U4L2 P5, both _ and __ should be the same
    # A2 : _ => protected __ => private，所以同個class裡面都可以存取，但是子類別只能存取_的屬性，無法存取__的屬性。

    # Q3 : According to the M2U4L2 P12, Override should not be allowed after adding final
    # A3 : final在python應該只是提示，而不會強制執行。

    # Q4 : In M2U4L2 P15, the same "簽名" can override the parent class method, and what about different parameter or return type?
    # A4 : 在Python中，方法的重載是根據參數的數量和類型來區分的，因此可以在子類別中定義相同名稱但參數不同的方法。