import random

RPS = ["rock", "paper", "scissors"]
player_choice = int(input("Please make your choise. Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
print(RPS[player_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")
print(RPS[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("Invalid number, you lose!")
elif player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0 and computer_choice == 1:
    print("Computer wins!")    
elif player_choice == 0 and computer_choice ==2:
    print("Player wins!")
elif player_choice == 1 and computer_choice == 0:
    print("Player wins")
elif player_choice == 1 and computer_choice == 2:
    print("Computer wins")
elif player_choice == 2 and computer_choice == 0:
    print("Computer wins")
elif player_choice == 2 and computer_choice == 1:
    print("Player wins")                   
