'''
# Snake Water Gun Game
1 for sanke
-1 for water
 0 for gun
'''
import random
print("Welcome to the Snake Water Gun Game!")
computer= random.choice([-1,0,1])

youstr=input("Enter your choice: ")
youDict={"s":1,
         "w":-1,
         "g":0}
reverseDict={1:"snake",
              -1:"water",
              0:"gun"}
you=youDict[youstr]
print(f"You chose:{reverseDict[you]} \n Computer chose: {reverseDict[computer]}")


if computer==-1 and you==1:
    print("You won!")
elif computer==1 and you==0:
    print("You loose!")
elif computer==1 and you==0:
    print("You won!")
elif computer==0 and you==1:
    print("You loose!")
elif computer==0 and you==-1:
    print("You won!")
elif computer==-1 and you==0:
    print("You loose!")
elif computer==-1 and you==-1:
    print("It's a tie!")
elif computer==1 and you==1:   
    print("It's a tie!")
elif computer==0 and you==0:
    print("It's a tie!")
elif computer==-1 and you==0:
    print("You won!")
elif computer==1 and you==-1:
    print("You loose!")
elif computer==0 and you==-1:
    print("You won!")
else:
    print("Something went wrong!")
# Note: The above code does not include the computer's choice logic.