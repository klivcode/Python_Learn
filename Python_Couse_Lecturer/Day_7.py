#Lists

Groups=["apple",
"banana",
"Gauva",
"Grapes"]   

print(Groups[0])
#Lists is mutable
Groups[0]="Kiwi"
print('\n',Groups[0])
print(Groups)

#append
Groups.append("Mango") #add at the end to the list
print(Groups)


#sort
l1=[1,34,78,8,0]
l1.sort()
print(l1)
#insert
l1.insert(2,345256) #insert at index 2
print(l1)

#reserve
l1.reverse()
print(l1)
#pop
l1.pop(2)#pop at index 2
print(l1)
#remove
l1.remove(78) #remove the particular element
print(l1)
#clear
l1.clear()
print(l1)


