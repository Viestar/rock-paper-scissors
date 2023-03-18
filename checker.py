# This is a module containing the functions for the Rock paper scissors game.

def match(player, computer):
    # Checking if a player's choice is the same as the random.
    if player == computer:
        print("\nWoooo! Its a tie, Nobody wins\n")

    # Incase a player picks scissors
    elif player == "scissors":
        # Case of rock from random, rock crashes the scissors, Player loses.
        if computer == "rock":
            print("\nYou lose, A rock crashed your scissors\n")
        # Case of paper from random, Player wins
        if computer == "paper":
            print("\nCongratulations. You cut the paper into pieces\n")

    # Incase a player pic ks rock
    elif player == "rock":

        # Case of paper from random, rock is covered, Player loses
        if computer == "paper":
            print("\nYou lose, the paper covered your rock buddy\n")

        # Case of scissors from random, Player wins, rock crashes scissors
        if computer == "scissors":
            print("\nCongratulations. Your rock crashed the scissors\n")

    # Incase a player picks paper
    elif player == "paper":

        # Case of scissors from random, paper is cut into pieces. Player loses
        if computer == "scissors":
            print("\nYou lose, your paper has been cut into pieces\n")

        # Case of rock from random, Player wins, paper covers the rock
        if computer == "rock":
            print("\nCongratulations. Your paper has covered the rock\n")
