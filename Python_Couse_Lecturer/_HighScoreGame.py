import random

def game():
    print("You are playing a high score game!")
    score=random.randint(1, 10000)

    #fetch the high score from the file
    with open("files/hs.txt") as file:
        high_score=file.read()
        if high_score!="":
            high_score=int(high_score)
        else:
            high_score=0
    print(f"Your High score is {high_score}")


    if score>high_score:
        print(f"Congratulations! You have set a new high score of {score}!")
        with open("files/hs.txt", "w") as file:
            file.write(str(score))
    

game()