# Number Guessing Game 1.0 - By Alexander Eraso Adarme

import random

# ToDo 1: Generate a random number using random from 1 to 100
random_number = random.randint(0, 101)

# ToDo 2: Let the user select the difficulty and take a guess:
difficulty = input("Pick the difficulty: H (5 lives), M (10 lives), E (15 Lives) \n").lower()

# Dictionary that contains the lives.
lives_dict = {"h": 5, "m":10, "e":15}
user_lives = lives_dict[difficulty]
print(f"You only have {user_lives} lives.")

user_guess = int(input("Guess a number between 1 and 100: "))

# ToDo 3: Make a loop so that the game repeats until user finds a solution.
guess = True
while guess:
    # ToDo 4: Check user's guess and provide some hints + break loop if guess is right.
    if user_guess == random_number:
        print("You got it!")
        guess = False
        break
    elif user_guess < random_number:
        print("Too low!")
    elif user_guess > random_number:
        print("Too high!")

    # ToDo 6: Check the user lives and tell them how many they got left - check if they ran out of lives
    if user_lives == 0:
        guess = False
        break
    # ToDo 5: Let the user try again and take 1 live away.
    user_lives -= 1
    print(f"You have {user_lives} left.\n")
    user_guess = int(input("Try again: "))
