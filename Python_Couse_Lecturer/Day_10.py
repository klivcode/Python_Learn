#dictionary
d={} #empty dictionary
marks={
    "Kliv":100,
    "Rahul":90,
    "Rohit":80
}
print(marks,type(marks))
print(marks["Kliv"])
#properties of dictionaries
#unordered
#mutable
#indexed
#can not be duplicated keys

#DIctionaries Methods
#1. get()
print(marks.get("Kliv"))    #prints value of key
#2. keys()
print(marks.keys()) #prints all keys

#3. values()
print(marks.values())    #prints all values

#4. items()
print(marks.items())     #prints all keys and values

#5. update()
marks.update({"Kliv":99})   #updates value of key
print(marks)

#6. pop()
marks.pop("Rahul")   #removes item with specified key
print(marks)

#7. popitem()
marks.popitem() #removes last item