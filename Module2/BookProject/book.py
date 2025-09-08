from enum import Enum
class Category(Enum):
    artBook = 1
    engBook = 2
class Book():
    #Book Constructor
    def __init__(self, bookName, noOfCopies, bookType):
        self.bookName = bookName
        self.noOfCopies = noOfCopies
        self.bookType = bookType

    #Getters
    def getName(self):
        return self.bookName

    def getCopies(self):
        return self.noOfCopies

    def getBookType(self):
        return self.bookType
    def changeNoOfCopies(self, count): #Changes number of copies
        self.noOfCopies = count
    def displayBook(self): #function will be overridden
        pass