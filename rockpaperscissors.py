# rock paper scissors python game 

import random 

while True: 
    yourchoice = input("Select a choice between rock, paper, or scissors: ")
    choices = ["rock", "paper", "scissors"]
    computerchoice = random.choice(choices)
    print(f"\n You chose {yourchoice} while the computer chose {computerchoice}.\n")

    if yourchoice == computerchoice:
        print(f"You and the computer both selected {yourchoice}")
    elif yourchoice == "rock":
        if computerchoice == "scissors":
            print("Rock beats scissors, you won!")
        else:
            print("Paper beats rock, you lose :(")
    elif yourchoice == "paper":
        if computerchoice == "rock":
            print("Paper beats rock, you win!")
        else:
            print("Scissors beats paper, you lose :(")
    elif yourchoice == "scissors":
        if computerchoice == "paper":
            print("Scissors beats paper, you win!")
        else:
            print("Rock beats scissors, you lose :(")
    playagain = input("Would you like to play again? (y/n): ")
    if playagain.lower() != "y":
        break
