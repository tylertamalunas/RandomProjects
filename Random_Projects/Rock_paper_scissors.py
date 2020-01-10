"""
Rock, paper, scissors game!
The computer will generate randomly one of the three options, and the user will have to beat them.
Rock beats scissors.
Scissors beats paper.
Paper beats rock.
Paper > Rock > Scissors > Paper
When the player types 'done' the game ends and the program stops.
"""
from random import choice

computer_options = ['rock', 'paper', 'scissors']
print("Let's play rock, paper, scissors! See if you can beat me.")
print("We'll play until you type 'done'.")
playing = True
while playing is True:
    computer_shoot = choice(computer_options)
    user_shoot = input("Your choice: ").lower()
    if user_shoot == 'rock':
        print(f"You: {user_shoot}")
        if user_shoot == computer_shoot:
            print(f"Me: {computer_shoot}")
            print("Tie Game!")
        elif computer_shoot == 'paper':
            print(f"Me: {computer_shoot}")
            print("You lost")
        elif computer_shoot == 'scissors':
            print(f"Me: {computer_shoot}")
            print("You beat me!")
    elif user_shoot == 'paper':
        print(f"You: {user_shoot}")
        if user_shoot == computer_shoot:
            print(f"Me: {computer_shoot}")
            print("Tie Game!")
        elif computer_shoot == 'scissors':
            print(f"Me: {computer_shoot}")
            print("You lost")
        elif computer_shoot == 'rock':
            print(f"Me: {computer_shoot}")
            print("You beat me!")
    elif user_shoot == 'scissors':
        print(f"You: {user_shoot}")
        if user_shoot == computer_shoot:
            print(f"Me: {computer_shoot}")
            print("Tie Game!")
        elif computer_shoot == 'rock':
            print(f"Me: {computer_shoot}")
            print("You lost")
        elif computer_shoot == 'paper':
            print(f"Me: {computer_shoot}")
            print("You beat me!")
    elif user_shoot == 'done':
        print("You've had enough. The game is over.")
        break
    else:
        print("You need to pick rock, paper, or scissors...")
