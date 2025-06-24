# map is used to apply a function to all items in an iterable
# map example
l=[1,2,3,4,5,6]

square=lambda x: x * x

squaredList=map(square, l)

print(list(squaredList))

#Filter is used to filter items in an iterable based on a condition
#filter example

def even(n):
    if(n%2==0):
        return True
    return False
onlyEven=filter(even, l)
print(list(onlyEven))


# reduce function is used to apply a function cumulatively to the items of an iterable, reducing it to a single value
# Reduce example

from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, l))
