# Module to use in making the game fun by selecting random choices
import random

# Checker is a module i have created with a fucntion match to carry
# out the task of matching Player input and Computer randomly generated choice
from checker import match

# saving the three hand gestures into a list.
source = ["rock", "paper", "scissors"]

# Using the random module to a pick a choice at random
computer = random.choice(source)

#initialising player
player = None

# Loop that will re-prompt a user until exactly one of the choices is entered.
while player not in source:
    #Prompting the user for input
    player = input("Enter either rock, paper or scissors: ")
    player.lower()

# Calling the match function from the checker module.
match(player, computer)


