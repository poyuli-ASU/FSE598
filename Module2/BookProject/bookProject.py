# Book Project consisting of multiple files:
# bookProject.py, Book.py, ArtBook.py, EngBook.py, and container.py
from book import *
from container import *
from artBook import *
from engBook import *
#Initialized bookList
bookList = None
#Searchs for the given book name
def searchBook(name):
    #Grant access to global variable
    global bookList
    #Creates a bookList copy
    temp = bookList;
    #Loop until all books are checked.
    #return book name or None
    while(temp!=None):
        if(temp.Book.getName()==name):
            return temp.Book;
        temp = temp.next;
    return None;

#Changes the number of copies of a given book
def changeNumberOfCopies(b,count):
    b.changeNoOfCopies(count);

#Adds a book to the list
def addBook(name_input, copies_input, type):
    #Given access to global bookList
    global bookList
    #Create a copy of bookList
    temp = bookList;
    #Changes type to an actual Category
    if(type == Category.artBook):
        b = ArtBook(name_input, copies_input, type);
    elif(type == Category.engBook):
        b = EngBook(name_input, copies_input, type);
    #Check if there are any books in the bookList and if not makes a new Container and sets
    # bookList to that container
    if(bookList == None):
        bookList = Container();
        bookList.Book = b;
        bookList.next = None;
        return;

#Display the bookList
def displayBooks():
    global bookList
    temp = bookList
    while temp != None:
        print(temp.Book.getName())
        temp = temp.next

#Saves the bookList
def save(fileName):
    global bookList #Gives access to global bookList
    temp = bookList #Creates a temp variable to bookList
    count = 0
    #Counts the number of books
    while temp != None:
        count += 1
        temp = temp.next
    #Open the file for writing
    try:
        fileBuf = open(fileName, "w") 
        temp = bookList # Resets temp to be a copy of bookList
        fileBuf.write(str(count)+"\n") #Save count first 
        # Loops through and adds the elements of each book 
        # Save (1)name (2)copies (3)type
        while(temp!=None):
            fileBuf.write(temp.Book.getName()+"\n")
            fileBuf.write(str(temp.Book.getCopies())+"\n")
            fileBuf.write(str(temp.Book.getBookType())+"\n")
            temp = temp.next
        fileBuf.close()
    except FileNotFoundError:
        print(f"File {fileName} not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if fileBuf:
            fileBuf.close()

# Loads existing books
def load(filename):
    global bookList #Gives access to global bookList
    temp = bookList #Creates a temp variable to bookList
    count = 0
    #Tries to open the file, if there is no file it does nothing
    try:
        #Read file
        fileBuf = open(filename, "r")
        #Gets the number of books
        count = int(fileBuf.readline())
        #Sets index to 0
        index = 0
        #Adds each book
        for i in range(count):
            #Creates a new container
            con = Container()
            #Resets temp to be a copy of bookList
            temp = bookList
            #Get names, copies, and type
            name = fileBuf.readline().strip()
            copies = int(fileBuf.readline().strip())
            bookType = fileBuf.readline().strip()
            if bookType == "artBook":
                b = ArtBook(name, copies, Category.artBook)
            elif bookType == "engBook":
                b = EngBook(name, copies, Category.engBook)
            addBook(b.getName(), b.getCopies(), b.getBookType())
        fileBuf.close()
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if fileBuf:
            fileBuf.close()