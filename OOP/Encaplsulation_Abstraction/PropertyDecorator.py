# Propert decorator is used to manage the acces to an attribute
# and to add validation logic when setting or getting the value of an attribute.
    # instance attribute || self.name
    # class attribute || Employee.company
class Employee:
    a=1

    @classmethod
    def show(cls):
        print(f"I am an employee {cls.a}")
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    @name.setter
    def name(self,value):
        self.first_name=value.split(" ")[0]
        self.last_name=value.split(" ")[1]
    

e=Employee()
e.name="John Doe"

print(e.name)  # Output: John Doe
print(e.first_name)  # Output: John 
print(e.last_name)  # Output: Doe

