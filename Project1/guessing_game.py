"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    print("Welcome to the number guessing game! Let's begin...")
    guess_number = ""
    random_number = random.randint(1,10)
    game = 0
    count = 1
    score_list = []
    while guess_number == "":
        try:
            guess_number = int(input("Please guess a number from 1 to 10: "))
        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")

    while guess_number != random_number:
        count+=1
        try:
            if guess_number > 10 or guess_number < 1:
                print("Your number was not between 1 to 10.")
            elif guess_number > random_number:
                print("It is lower.")
            elif guess_number < random_number:
                print("It is higher.")
            guess_number = int(input("Try again: "))

        except ValueError:
            print("Oops!  That was not a valid number.  Try again...")
    print(f'Congratulations! You got it. It only took you {count} try(ies). The game is now over.')
    score_list.append(count)
    print("Your high score is", score_list[0], ". Number in list: ", len(score_list))
    
    play_again = str(input("See if you can beat your score. Play again? yes or no: ").lower())
    
    if play_again == "yes":
        start_game()
        
    else:
        print("Thanks for playing!")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()