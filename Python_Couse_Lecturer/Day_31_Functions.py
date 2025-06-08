
#functions

def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")

greet("Alice")



# deafault parameters

def goodDay(name, ending="Thanks for coming!"):
    """This function greets the person passed in as a parameter with a default ending."""
    print("Good day, " + name + ". " + ending)

goodDay("Bob")