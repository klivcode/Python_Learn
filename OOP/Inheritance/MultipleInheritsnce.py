#Multiple 

class A:
    def display(slef):
        print("Class A")
    
class B:
    def display1(self):
        print("Class B")

class derived(A, B):
    def displayDerived(self):
        print("Derived Class")

d=derived()
d.display()  # This will call the display method from class A, as it is the first parent class
d.display1()  # This will call the display1 method from class B
d.displayDerived()  # This will call the displayDerived method from the derived class