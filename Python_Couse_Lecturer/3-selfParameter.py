class employee:
    language = "Python"  # class attribute || static attribute
    salary = 100000

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")

    @staticmethod
    def greet():
        print("Hello, welcome to the employee class!")



kliv = employee()
employee.getinfo(kliv)
#or
kliv.getinfo()
kliv.greet()  # calling static method using instance