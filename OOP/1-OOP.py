class Employee:
    language = "Python" # class attribute || static attribute
    salary = 100000

kliv = Employee()
kliv.name = "Klivcode" # object attribute || instance attribute
print(kliv.name, kliv.language, kliv.salary)

ram = Employee()
ram.name = "Ram"
print(ram.name, ram.language, ram.salary)