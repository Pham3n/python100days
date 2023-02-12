# Rock Paper Scissors

import random

print("S beats P     R beats S       P beats R")
options = ["Rock", "Paper", "Scissors"]
score = 0

def choices(options, score):
    pcchoice = random.choice(options)

    uchoice = input("Choose between Rocks, Paper and Scissors.\nOnly type 'R', 'P', 'S' or 'E' to exit")

    print(f"You chose {uchoice}")
    if uchoice == "E" : phuma(score)
    print(f"Computer chose {pcchoice}")

    calculator(options, uchoice, pcchoice, score)

def calculator(options, uchoice, pcchoice, score):
#    print(uchoice)
#    print(type(uchoice))
    if uchoice == "R" :
        if pcchoice == "Rock" :
            print("Draw")
        elif pcchoice == "Paper" : 
            print("You loose")
            score -= 1
        elif pcchoice == "Scissors" : 
            print("You WIN")
            score += 1
    elif uchoice == "P" :
        if pcchoice == "Rock" :
            print("You WIN")
            score += 1
        elif pcchoice == "Paper" : 
            print("Draw")
            score = score
        elif pcchoice == "Scissors" : 
            print("You loose")
            score -= 1
    elif uchoice == "S" :
        if pcchoice == "Rock" :
            print("loose")
            score -= 1
        elif pcchoice == "Paper" : 
            print("You WIN")
            score += 1
        elif pcchoice == "Scissors" : 
            print("Draw")
            score = score
    else : 
        print("Invalid choice")
    choices(options, score)

def phuma(score) :
    print(f"You have chosen to exit.\n You score is {score}")
    exit()

choices(options, score)