#Realtional Operators/ Comparison Operators
#used to compare the values
#==,!=,>,<,>=,<=
#returns boolean value
#True or False

#Logical Operators(AND,OR,NOT)
#Elif Clause
#Nested If-Else



#Example of Multiple If 
a= int(input("Enter the value of a:"))
#if statement number 1 which is inpendent
if a%2==0:
    print("a is even")

#second if statement which is dependent on first if statement
if a>10:
    print("a is greater than 10")
elif a<=2:
    print("a is less than or equal to 2")
else:
    print("a is odd")  