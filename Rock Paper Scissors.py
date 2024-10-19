import random
import time

print("Rock Paper Scissors Game")
print("First to 3 wins!")

time.sleep(3)

moves = ["rock", "paper", "scissors"]
current_wins = 0
computer_wins = 0

while True:

    print("\nPlayer: " + str(current_wins))
    print("Computer: " + str(computer_wins))
    
    while True:
        player_move = input("Enter your move: ").lower()
        if player_move in moves:
            break
        print("Invalid move!\n")

    print("Computer is picking a move...\n")
    thinking_time = random.randint(2, 5)
    time.sleep(thinking_time)
    computer_move = random.choice(moves)

    print("Rock", end=" ", flush=True)
    time.sleep(1)
    print("Paper", end=" ", flush=True)
    time.sleep(1)
    print("Scissors", end=" ", flush=True)
    time.sleep(2)
    print("SHOOT!\n")

    print("Player: " + player_move)
    print("Computer: " + computer_move + "\n")

    if player_move == "rock" and computer_move == "paper":
        print("You lost!")
        computer_wins += 1
    elif player_move == "rock" and computer_move == "scissors":
        print("You won!")
        current_wins += 1
    elif player_move == "paper" and computer_move == "rock":
        print("You won!")
        current_wins += 1
    elif player_move == "paper" and computer_move == "scissors":
        print("You lost!")
        computer_wins += 1
    elif player_move == "scissors" and computer_move == "paper":
        print("You won!")
        current_wins += 1
    elif player_move == "scissors" and computer_move == "rock":
        print("You lost!")
        computer_wins += 1
    else:
        print("Draw!")

    if current_wins == 3:
        print("Congratulations! You defeated the computer in a game of Rock Paper Scissors!")
        break
    elif computer_wins == 3:
        print("You lost a game of Rock Paper Scissors to a computer...")
        break