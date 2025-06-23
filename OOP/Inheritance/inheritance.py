class employee:
    def __init__(self, salary):
        self.salary = salary
    def show(self):
        print("I am an employee and my salary is", self.salary)

# class programmer:
#     def show(self):
#         print("I am a programmer")
    
#     def language(self):
#         print("I am a Python programmer")
    
#inheritance

class programmer(employee):
    
    def language(self):
        print("I am a Python programmer")

a=employee(50000)
b=programmer(60000)

print(a.show(),b.show(),b.language())