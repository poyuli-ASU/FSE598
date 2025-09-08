from typing import final

class person:
    name=""
    id=0
    address=""
    def __init__(self,name,id,address):
        self.name=name
        self.id=id
        self.address=address
    def display(self):
        print(f"Name:{self.name}, ID:{self.id}, Address:{self.address}")

class student(person):
    school =""
    courseList = []
    gpa = 0.0
    def __init__(self, school, courseList, gpa):
        person.__init__(self,name,id,address)
        self.school=school
    def addCourse(self,course):
        self.courseList.append(course)
    def display(self):
        print(f"Name:{self.name}, ID:{self.id}, Address:{self.address}")
        print(f",School:{self.school}, CourseList:{self.courseList}, GPA:{self.gpa}")    

class employee(person):
    school=""
    title=""
    def __init__(self, school, title):
        person.__init__(self,name,id,address)
        self.school=school
        self.title=title
    def display(self):
        print(f"Name:{self.name}, ID:{self.id}, Address:{self.address}")
        print(f",School:{self.school}, Title:{self.title}")

class undergrad(student):
    courseList = []
    def __init__(self, year):
        student.__init__(self,name,id,address,school)
    def display(self):
        print(f"Name:{self.name}, ID:{self.id}, Address:{self.address}")
        print(f",School:{self.school}, CourseList:{self.courseList}, GPA:{self.gpa}, Year:{self.gpa}")

class grad(student):
    advisor=""
    courseList = []
    def __init__(self, name, id, address, school, advisor):
        super().__init__(self, name, id, address, school)
        self.advisor
    def display(self): 
        print(f"Name:{self.name}, ID:{self.id}, Address:{self.address}")
        print(f", School:{self.school}, CourseList:{self.courseList}, GPA:{self.gpa}, Advisor:{self.advisor}")

class ta(student, employee):
    sSchool=""  
    eSchool=""
    courseList = []
    def __init__(self, name, id, address, sSchool, eSchool, title):
        sSchool = ""
        eSchool = ""                                #Q6 : Why redefine the sSchool, and eSchool variables here?
        student.__init__(self,name,id,address,sSchool)
        employee.__init__(self,eSchool,title)
    def display(self):
        print(f"Name:{self.name}, ID:{self.id}, Address:{self.address}")
        print(f", sSchool:{self.sSchool}, CourseList:{self.courseList}, GPA:{self.gpa}, Advisor:{self.advisor}")
        print(f", eSchool:{self.eSchool}, Title:{self.title}")

class faculty(employee):
    research=""
    def __init__(self, name, id, address, school, title, research):
        employee.__init__(self, school, title)
        self.research=research
    def display(self):
        print(f"name={self.name}, id={self.id}, address={self.address}, school={self.school}, title={self.title}")
        print(f", Research:{self.research}")

personList = []

def executeAction(c):
    if(c=="P"):
        name = input("Enter the person's name")
        if(searchPerson(name)==None):
            id = input("Enter the person's ID")
            address = input("Enter the person's address")
            addPerson(name,id,address)
            print('Person added successfully.')
        else:
            print('Person already exists.')
    elif(c=="S"):
        name = input("Enter the student's name")
        if(searchStudent(name)==None):
            id = input("Enter the student's ID")
            address = input("Enter the student's address")
            school = input("Enter the student's school")
            addStudent(name,id,address,school)
            print('Student added successfully.')
        else:
            print('Student already exists.')
    elif(c=="E"):
        name = input("Enter the employee's name")
        if(searchEmployee(name)==None):
            id = input("Enter the employee's ID")
            address = input("Enter the employee's address")
            school = input("Enter the employee's school")
            title = input("Enter the employee's title")
            addEmployee(name,id,address,school,title)
            print('Employee added successfully.')
        else:
            print('Employee already exists.')
    elif(c=="G"):
        name = input("Enter the graduate student's name")
        if(searchGradStudent(name)==None):
            id = input("Enter the graduate student's ID")
            address = input("Enter the graduate student's address")
            school = input("Enter the graduate student's school")
            advisor = input("Enter the graduate student's advisor")
            addGradStudent(name,id,address,school,advisor)
            print('Graduate student added successfully.')
        else:
            print('Graduate student already exists.')
    elif(c=="U"):
        name = input("Enter the undergraduate student's name")
        if(searchUndergradStudent(name)==None):
            id = input("Enter the undergraduate student's ID")
            address = input("Enter the undergraduate student's address")
            school = input("Enter the undergraduate student's school")
            year = input("Enter the undergraduate student's year")
            addUndergradStudent(name, id, address, school, year)
            print('Undergraduate student added successfully.')
        else:
            print('Undergraduate student already exists.')
    elif(c=="T"):
        name = input("Enter the teaching assistant's name")
        if(searchTA(name)==None):
            id = input("Enter the teaching assistant's ID")
            address = input("Enter the teaching assistant's address")
            school = input("Enter the teaching assistant's school")
            course = input("Enter the teaching assistant's course")
            addTA(name, id, address, school, course)
            print('Teaching assistant added successfully.')
        else:
            print('Teaching assistant already exists.')
    elif(c=="F"):
        name = input("Enter the faculty member's name")
        if(searchFaculty(name)==None):
            id = input("Enter the faculty member's ID")
            address = input("Enter the faculty member's address")
            school = input("Enter the faculty member's school")
            title = input("Enter the faculty member's title")
            research = input("Enter the faculty member's research")
            addFaculty(name,id,address,school,title,research)
            print('Faculty member added successfully.')
        else:
            print('Faculty member already exists.')
    elif(c=="C"):
        name=input("Enter the student's name")
        i = searchPerson(name)
        if(i==-1):
            print("Student not found.")
        elif isinstance(personList[i],student) or issubclass(type(personList[i]),student):
            course = input("Enter the course to add")
            gp = input("Enter the GPA")
            courses = Len( personList[i].courseList )
            personList[i].gpa = round( ( personList[i].gpa * courses + gp ) / ( courses + 1 ) , 2)
            personList[i].addCourse(course)
            print("Course added successfully.")
        else:
            print("The person is not a student.")
    elif(c=="D"):
        displayList(personList)
    elif(c=="R"):
        name = input("Enter the person's name to remove")
        i = searchPerson(name)
        if(i==-1):
            print("Person not found.")
        else:
            removePerson(name)
            print("Person removed successfully.")

def addPerson(name, id, address):   #Adds person to personList
    p = person(name, id, address)
    personList.append(p)
def addStudent(name, id, address, school):  #Adds student to personList
    s = student(school, [], 0.0)
    s.name = name
    s.id = id
    s.address = address
    personList.append(s)
def addEmployee(name, id, address, school, title): #Adds employee to personList
    e = employee(school, title)
    e.name = name
    e.id = id
    e.address = address
    personList.append(e)
def addGradStudent(name, id, address, school, advisor): #Adds grad student to personList
    g = grad(name, id, address, school, advisor)
    personList.append(g)
def addUndergradStudent(name, id, address, school, year): #Adds undergrad student to personList
    u = undergrad(name, id, address, school, year)
    personList.append(u)
def removePerson(name): #Removes person from personList
    i = searchPerson(name)
    if(i!=-1):
        personList.pop(i)
def addFaculty(name, id, address, school, title, research): #Adds faculty to personList
    f = faculty(name, id, address, school, title, research)
    personList.append(f)
def addTA(name, id, address, school, course): #Adds teaching assistant to personList
    ta = teachingAssistant(name, id, address, school, course)
    personList.append(ta)

def displayList(list):
    for person in list:
        print(person)

def main():
    while True:
        print("1. Add Person")
        print("2. Add Student")
        print("3. Add Employee")
        print("4. Add Graduate Student")
        print("5. Add Undergraduate Student")
        print("6. Remove Person")
        print("7. Display List")
        print("8. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            id = input("Enter ID: ")
            address = input("Enter address: ")
            addPerson(name, id, address)
        elif choice == "2":
            name = input("Enter name: ")
            id = input("Enter ID: ")
            address = input("Enter address: ")
            school = input("Enter school: ")
            addStudent(name, id, address, school)
        elif choice == "3":
            name = input("Enter name: ")
            id = input("Enter ID: ")
            address = input("Enter address: ")
            school = input("Enter school: ")
            title = input("Enter title: ")
            addEmployee(name, id, address, school, title)
        elif choice == "4":
            name = input("Enter name: ")
            id = input("Enter ID: ")
            address = input("Enter address: ")
            school = input("Enter school: ")
            advisor = input("Enter advisor: ")
            addGradStudent(name, id, address, school, advisor)
        elif choice == "5":
            name = input("Enter name: ")
            id = input("Enter ID: ")
            address = input("Enter address: ")
            school = input("Enter school: ")
            year = input("Enter year: ")
            addUndergradStudent(name, id, address, school, year)
        elif choice == "6":
            name = input("Enter name: ")
            removePerson(name)
        elif choice == "7":
            displayList(personList)
        elif choice == "8":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


    # Q5 : due to school is defined in both parents' attributes, so can not use the same name; however, what about grand parent?
    # A5 : MRO (Method Resolution Order) determines ALL conflicts. The closer class will be used.