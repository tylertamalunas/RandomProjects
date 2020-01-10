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
computer_wins = 0
user_wins = 0

while playing is True:
    computer_shoot = choice(computer_options)
    print("==Games won==")
    print(f"You: {user_wins}    Me: {computer_wins}")
    user_shoot = input("Your choice: ").lower()
    if user_shoot == 'rock':
        print(f"You: {user_shoot}")
        if user_shoot == computer_shoot:
            print(f"Me: {computer_shoot}")
            print("Tie Game!\n")
        elif computer_shoot == 'paper':
            print(f"Me: {computer_shoot}")
            print("You lost.\n")
            computer_wins += 1
        elif computer_shoot == 'scissors':
            print(f"Me: {computer_shoot}")
            print("You beat me!\n")
            user_wins += 1
    elif user_shoot == 'paper':
        print(f"You: {user_shoot}")
        if user_shoot == computer_shoot:
            print(f"Me: {computer_shoot}")
            print("Tie Game!\n")
        elif computer_shoot == 'scissors':
            print(f"Me: {computer_shoot}")
            print("You lost.\n")
            computer_wins += 1
        elif computer_shoot == 'rock':
            print(f"Me: {computer_shoot}")
            print("You beat me!\n")
            user_wins += 1
    elif user_shoot == 'scissors':
        print(f"You: {user_shoot}")
        if user_shoot == computer_shoot:
            print(f"Me: {computer_shoot}")
            print("Tie Game! \n")
        elif computer_shoot == 'rock':
            print(f"Me: {computer_shoot}")
            print("You lost. \n")
            computer_wins += 1
        elif computer_shoot == 'paper':
            print(f"Me: {computer_shoot}")
            print("You beat me! \n")
            user_wins += 1
    elif user_shoot == 'done':
        print("You've had enough. The game is over.")
        print("==FINAL SCORE==")
        print(f"You: {user_wins}    Me: {computer_wins}")
        if user_wins > computer_wins:
            print("You won this time...")
        elif user_wins < computer_wins:
            print("Of course I won, did you think you could beat a computer?")
        else:
            print("We'll have to settle this next time I guess.")
        break
    else:
        print("You need to pick rock, paper, or scissors...")
