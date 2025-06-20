class Employee:
    language = "Python" # class attribute || static attribute
    salary = 100000

kliv = Employee()
kliv.name = "Klivcode"  # changing object attribute for this instance
kliv.language = "Java"  # changing class attribute for this instance
print(kliv.name, kliv.language, kliv.salary)

ram = Employee()
ram.name = "Ram"
ram.language = "JavaScript"  # changing class attribute for this instance
print(ram.name, ram.language, ram.salary)