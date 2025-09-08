def main():
    print("Hello World")

def averageOfList(num):
    assert isinstance(num, list), "Input should be a list"
    sumOfNumbers = 0
    for t in num:
        sumOfNumbers += t
    averageOfList = sumOfNumbers / len(num)
    return averageOfList
def isEven(value:int):
    if not isinstance(value, int):
        raise TypeError("Input should be an integer")
    
    print(value)
    if value % 2 == 0:
        return True
    else:
        return False
    
def addNumbers(first, second, third = 0, forth = 0):
    return first + second + third + forth

def printInfo(name, age):
    print("Name:", name)
    print("Age:", age)
    return;

def addThemAll(*args):
    return sum(args)

if __name__ == "__main__":
    main()
    print(addThemAll(1, 2, 3))
    print(addThemAll(4, 5, 6, 7))
