#list problem

l=["apple","banana","cherry","kiwi","mango"]

name=input("Enter the name:")
lowerCaseName=name.lower()
if lowerCaseName in l:
    print("Name is present in list")
else:
    print("Name is not present in list")
