#using walrus operator
# The walrus operator allows assignment within an expression
# and is useful for reducing code duplication.
# Example of using the walrus operator
# The walrus operator (:=) allows assignment within an expression

if(n:=10):
    print(n)

if(n:=len("Hello, World!")):
    print(n)