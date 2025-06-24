# List Comprehensions

myList=[1,2,3,4,5,6,7,8,9,10]

squaredList=[]
for item in myList:
    squaredList.append(item*item)

print(squaredList)


# can be done using list comprehensions

squaredList=[item*item for item in myList]
print(squaredList)