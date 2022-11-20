# This is a guessing game, Where the user has to guess the number that has been generated randomly.
import random

top_of_range = input("type a number")

if top_of_range.isdigit():  # checking if the input is a number
    top_of_range = int(top_of_range)  # int is used to convert str to int
    if top_of_range <= 0:
        print('please type a number lager than 0')
        quit()
else:
    print('please type a number next time')
    quit()

random_number = random.randrange(0, top_of_range)  # can also use randint
guess = 0
while True:  # we can also use while user_guess != random_number
    guess += 1
    user_guess = input('Make a guess')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a valid number")
        continue

    if user_guess == random_number:
        print("congrdulations you got it right ")
        break
    else:  # we can also use "elif user_guess > random_number"
        if user_guess > random_number:
            print("You were above the above the number")
        else:
            print("you were below the number")
print("you got it", guess, "guess")
