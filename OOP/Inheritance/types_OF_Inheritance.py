# Single Inheritance

class Parent:
    def __init__(self):
        self.parent_attribute = "I am a parent attribute"

    def parent_method(self):
        return "This is a method from the parent class"

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.child_attribute = "I am a child attribute"

    def child_method(self):
        return "This is a method from the child class"


c=Child()
print(c.parent_attribute)  # Accessing parent attribute
print(c.child_attribute)   # Accessing child attribute
print(c.parent_method())   # Calling parent method
print(c.child_method())    # Calling child method