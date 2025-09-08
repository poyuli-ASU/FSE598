from enum import Enum
from book import *

class EngBook(Book):
    #EngBook Constructor that implements Book constructor
    def __init__(self, bookName, noOfCopies, bookType):
        super().__init__(bookName, noOfCopies, bookType)

    #Display Book's info. It overrides the base class's function
    def displayBook(self):
        print("Book name:", self.bookName)
        print("Number of Copies:", self.noOfCopies)
        print("Book Type:", self.bookType)