import random

class RPS:

    def __init__(self, rps):
        self.rps = rps

    def data_input(self):
        player_choice = input("Please make your choise. Type 0 for Rock, 1 for Paper or 2 for Scissors (q to quit): \n")
        return player_choice

    def player_choice(pc):
        player_choice = int(pc)
        return player_choice

    def computer_choice(self):
        computer_choice = random.randint(0,2)
        return computer_choice
    
    def except_errors(self):
        pass

    def play_game(self):
        pass

    def main(self):
        pc = self.data_input()
        cc = self.computer_choice()

    if __name__ == '__main__':
        pass


# import sys
# import random
# 
# RPS = ["rock", "paper", "scissors"]
# 
# while True:
#     try:
#         player_choice = input("Please make your choise. Type 0 for Rock, 1 for Paper or 2 for Scissors (q to quit): \n")
#         if player_choice.lower() == 'q':
#             print("Bye")
#             break
#         player_choice = int(player_choice)
#     except ValueError:
#         print("This is not a number")
#         continue
#     if player_choice >= 3 or player_choice < 0:
#         print("Invalid number, you lose!")
#     else:
#         computer_choice = random.randint(0,2)
# 
#         print("Player:", RPS[player_choice])
#         print("Computer:", RPS[computer_choice])
# 
#         if player_choice == computer_choice:
#             print("It's a draw")
#         elif player_choice == 0 and computer_choice == 1:
#             print("Computer wins!")
#         elif player_choice == 0 and computer_choice ==2:
#             print("Player wins!")
#         elif player_choice == 1 and computer_choice == 0:
#             print("Player wins")
#         elif player_choice == 1 and computer_choice == 2:
#             print("Computer wins")
#         elif player_choice == 2 and computer_choice == 0:
#             print("Computer wins")
#         elif player_choice == 2 and computer_choice == 1:
#             print("Player wins")
             
