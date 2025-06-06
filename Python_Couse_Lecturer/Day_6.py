name=input("Enter the name")

print(f"Good Afternoon {name}") #f string (new method)
#another method
print("Good Afternoon {}".format(name))
print("Good Afternoon %s" %name)
print("Good Afternoon",name)
print("Good Afternoon "+name)
print("Good Afternoon",name,"How are you")



letter=''' Dear <|Name|>
You are selected!
Date: <|Date|> '''

print(letter.replace("<|Name|>","KlivCode").replace("<|Date|>","12/12/2025")) #chaining of replace function in one line


# detct the double space in the string
doubleSpcae="Hello KlivCode  i AM FINE"
SingleSpcae="Hello KlivCode i AM FINE"
print(doubleSpcae.find("  "))
print(SingleSpcae.find("  "))

#replace the double space with single space
print(doubleSpcae.replace("  "," "))
#remove the space from the string
print(doubleSpcae.replace(" ",""))
#remove the space from the string
print(doubleSpcae.strip())