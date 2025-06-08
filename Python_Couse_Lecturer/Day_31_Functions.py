
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

# function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print("The sum is:", result)

# recursion

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n* fact(n-1)
    

def main():
    number = int(input("Enter a number to find its factorial: "))
    result = fact(number)
    print(f"The factorial of {number} is {result}") #f-string for formatting 

main()