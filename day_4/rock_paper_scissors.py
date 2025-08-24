import random

print("Welcome to the game of Rock, Paper, Scissors!")
print("Type 0 for Rock, 1 for Paper, and 2 for Scissors.")

def rock_paper_scissors(player):
    if player == 0:
        print("Rock")
    elif player == 1:
        print("Paper")
    else:
        print("Scissors")

num = [0,1,2]

player1 = int(input("Player 1: "))
rock_paper_scissors(player1)

computer = random.randint(0, len(num) - 1)
rock_paper_scissors(computer)


if player1 <= 2:
    if player1 == computer:
        print("Draw!")
    elif player1 == 0 and computer == 2:
        print("Player 1 wins!")
    elif player1 == 1 and computer == 0:
        print("Player 1 wins!")
    elif player1 == 2 and computer == 1:
        print("Player 1 wins!")
    else:
        print("Computer wins!")
else:
    print("Invalid input")