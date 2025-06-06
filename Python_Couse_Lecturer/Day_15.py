#Condtional Expression (if else and if elif else ladder)

user=int(input("Enter you age: "))
if user>=18: #colon is must used to know that the next line is part of if condition
    print("You can vote")
else:
    print("You can not vote")

print(f"Your age is {user}")# f format


# if elif else ladder Conditional Expression 

user1=int(input("Enter you age: "))
if user1>=18:
    print("You can vote")
elif user1<=10:
    print("Go and Enjoy the childhood")
else:
    print("You can not vote") # left space is indented


print("End Of Program")