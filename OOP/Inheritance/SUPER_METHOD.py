#super method

class Employee:
    a=1
    def __int__(self):
        print("Employee constructor called")
    
class Programmer(Employee):
    b=2
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        print("Programmer constructor called")

class Manager(Programmer):
    c=3
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        print("Manager constructor called")


o=Manager()
print(o.a,o.b, o.c)
# to call the constructor of parents class, uncomment the super() lines in the __init__ methods of Programmer and Manager.
