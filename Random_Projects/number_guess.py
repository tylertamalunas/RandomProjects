"""
Guess the number game! Computer will randomly generate a number from 0-20 and you need to guess what it is. It will tell
you if you guess too high or too low, and you get 3 tries.
"""
from random import randint

secret_number = randint(0, 20)
guess_count = 0
guess_limit = 3
print("Welcome to the Guessing Game! Let's see if you can get the number right within 3 tries. The number will be"
      "between 0 and 20")

while guess_count < guess_limit:
    user_guess = int(input('> '))
    guesses_left = guess_limit - guess_count
    if user_guess < 0 or user_guess > 20:
        print("Your number needs to be between 0 and 20!")
    if user_guess == secret_number:
        print("You guessed it!!!!")
        break
    elif user_guess < secret_number and guesses_left != 0 and user_guess >= 0 and user_guess <= 20:
        print("That's too low.")
        print(f"You have {guesses_left} guesses left.")
        guess_count += 1
    elif user_guess > secret_number and guesses_left != 0 and user_guess >= 0 and user_guess <= 20:
        print("That's too high.")
        print(f"You have {guesses_left} guesses left.")
        guess_count += 1

else:
    print("That was your last guess. You lost!!")
    print(f"The correct number was {secret_number}.")
