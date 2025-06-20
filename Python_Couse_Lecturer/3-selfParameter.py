class employee:
    language = "Python"  # class attribute || static attribute
    salary = 100000

    def getinfo(self):
        print(f"The language is {self.language} and salary is {self.salary}")


        
kliv = employee()
employee.getinfo(kliv)
#or
kliv.getinfo()