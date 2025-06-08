n=int(input("Enter the number: "))
for i in range (1,11):
    print(f"{n} x {i}={n*i}")
#using while do same 
i=1
while i<=10:
    print(f"{n} x {i}={n*i}")
    i+=1


#start with a
l=["apple","mango","banana"]

for i in l:
    if(i.startswith("a")):
        print(f"i love {i} ")