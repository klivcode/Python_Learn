# multilevel inheritance

class Employee:

    def show(self):
        print("I am an employee")
    
class Programmer(Employee):

    def showProgrammer(self):
        print("I am a programmer")

class Manager(Programmer):

    def showManager(self):
        print("I am a manager")

m= Manager()
m.show()  # From Employee
m.showProgrammer()  # From Programmer   
m.showManager()  # From Manager
