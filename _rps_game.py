# Date: 9/26/19

# This is a random module for the computer choice
import random

# This is just an introductory to let player know what game they are playing
print("\nHi Today you are going to be " +
      "playing a game of Rock, Paper, Scissors against the Computer!\n")

# the while loop is set to True so it can keeping looping until it is set to false
while True:

    # comp_choices is assign to a list containing rock, paper, and scissors
    comp_choices = ["rock", "paper", "scissors"]

    # comp is assign to comp_choices where the computer will be randomly picking its choices from comp_choices using
    # random.randint()
    comp = comp_choices[random.randint(0, 2)]

    # This is asking the user to enter in its choice to play against the computer
    user_choice = input("Enter Rock, Paper, Scissors to play:\n ").lower()

    # This while loop is checking if the user enters a choice that matches with the comp_choices list and if it doesn't
    # Its ask the user to enter again until the user enters in a right choice of Rock, Paper, Scissors
    while user_choice not in comp_choices:
        print("You did not enter Rock, Paper, or Scissors!")
        user_choice = input("Please Enter Your choice again:\n ").lower()

    # Once the while checks if the user enters in the right choice then it goes to the if/elif statement to see what the
    # user enters and the comp enters to see who won the game.
    if user_choice == comp:
        result = "Tie!"

    elif user_choice == "rock":
        if comp == "scissors":
            result = "You won!"
        else:
            result = "Computer won!"

    elif user_choice == "paper":
        if comp == "rock":
            result = "You won!"
        else:
            result = "Computer won!"

    elif user_choice == "scissors":
        if comp == "paper":
            result = "You won!"
        else:
            result = "Computer won!"

    # This 2 print statements gives an output of the result and the output of what the user choice was and what the
    # Computer Choice was
    print(result)
    print("User choice was", user_choice, "and Computer choice was", comp, "\n")

    # This is asking the player to if the player wants to play again or not, if the player says no than the loop breaks
    again = input("Would you like to Play again Y or N:\n ").upper()
    if again == "N":
        print("Thank you for playing the game.")
        print("Goodbye!")
        break
