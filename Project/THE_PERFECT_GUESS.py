
import random
n=random.randint(1, 100)
print("Welcome to THE PERFECT GUESS")
guesses=0
a=-1
while a!=n:
    
    a=int(input("Guess the number\n(1-100): "))

    if a>n:
        print("Lower number please")
        guesses+=1
    elif a<n:
        print("Higher number please")
        guesses+=1
    else:
        print(f"Congratulations! You've guessed the number in {guesses} attempts.")