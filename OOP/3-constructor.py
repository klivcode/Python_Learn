class Student:
    def __init__(self, name, age): # dunder method for constructor starting with double underscore
        self.name = name
        self.age = age

shiva = Student("Shiva", 20)
print(shiva.name, shiva.age)