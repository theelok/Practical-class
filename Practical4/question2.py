import random


while True:
    answer =random.randint(1,2)

    guess=int(input("Enter your guess as 1 for head,2 for atail, or 0 to exit:"))

    if guess==0:
        print("Thank for playing the games!\n")
        break
    elif guess==1 or guess==2:
        if guess== answer:
            print("You are correct") 
            break
        else : print("You are choosing wrong answer") 
        break
    else:print("Pls enter 1 or 2")