"""
Write a programme, which generates a random password for the user. Ask the user how long they want their password to be,
and how many letters and numbers they want in their password. Have a mix of upper and lowercase letters, as well as
numbers and symbols. The password should be a minimum of 6 characters long.
"""
from random import choice, randint, shuffle
from string import ascii_letters

password_digit = 0
alphabet = ascii_letters
letter = 0
password = []

while True:
    try:
        password_length = int(input("How long do you want your password to be? (min of 6 characters): "))
        letters = int(input("How many letters: "))

        while password_digit < password_length:
            password_digit += 1
            if letter < letters:
                letter += 1
                password.append(choice(alphabet))
            elif letter == letters:
                password.append(str(randint(0, 9)))
        else:
            shuffle(password)
            print("".join(password))
            break
    except ValueError:
        print("Please try a number.")

