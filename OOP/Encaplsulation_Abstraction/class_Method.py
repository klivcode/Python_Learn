class Employee:
    a=1
    @classmethod # class method decorator
    def show(cls):
        print(f"I am an employee {cls.a}")

e=Employee()
e.a=45
e.show() # I am an employee 45
