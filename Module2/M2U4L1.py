def main():
    alf = Pet("Alf",5)
    #moon = Pet("Moon",7)

    alf.breed = "Bulldog"
    #alf.modifier()
    alf.age = 6
    
    print(f"Alf __class__ is {alf.__class__.breed}")
    print(f"Alf breed is {alf.breed}")                  
    #print(f"Moon is a {moon.__class__.breed}")

    print("{} is {} years old".format(alf.name, alf.age))
    #print("{} is {} years old".format(moon.name, moon.age))

class Pet:
    # class attribute = C#的static屬性
    breed = "Chihuahua"
    # instance attribute = C#的一般屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def modifier(self):
        self.breed = "Bulldog"

if __name__ == "__main__":
    main()
    
# Q1:如果只宣告了class attribute一樣可以透過instance attribute來存取嗎?
# 可以，程式的優先順序是先找instance attribute，再找class attribute。
# 但是如果強行給予class attribute同名的instance attribute，則instance attribute會蓋掉class attribute。