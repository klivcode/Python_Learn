# Operator Overloading

class Number:
    def __init__(self,value):
        self.value=value

    def __add__(self,num):
        return self.value + num.value

n=Number(10)
m=Number(20)
# Overloading the '+' operator

print(n+m)