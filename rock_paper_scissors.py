import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissors"]

while True:
    user_input = input("type rock/paper/scissor or Q to quit").lower()
    if user_input == "q":
        quit()
    if user_input not in ["rock", "paper", "scissor"]:
        continue
    random_number = random.randint(0, 2)
# rock is 0,paper is 1, scissors is 2
    computer_pick = option[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    else:
        print("you Lost!")
        computer_wins += 1
print("You won", user_wins, "Times")
print("computer wins", computer_wins, "Times")
print("goodbye!")
