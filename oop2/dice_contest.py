#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()

    # track scores for both players
    swapper_score = 0
    loaded_dice_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    # if game number is less than number of games to run loop through script
    while game_number < number_of_games:
        #swapper script is run
        swapper.roll()
        # dice load script is run
        loaded_dice.roll()
        
        #cheating script run
        swapper.cheat()
        loaded_dice.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()):
            #print("Draw!")
            #do not add to either score
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()):
            #print("Dice swapper wins!")
            # increase swapper score by 1
            swapper_score+= 1
        else:
            #print("Loaded dice wins!")
            #increase loaded score by 1
            loaded_dice_score += 1
        # increase the game number by 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")

    # determine the winner
    # if the game is a draw
    if swapper_score == loaded_dice_score:
        print("Game was drawn")
    # if the swapper won more than the loaded dice
    elif swapper_score > loaded_dice_score:
        print("Swapper won most games")
    # if the loaded won more games
    else:
        print("Loaded dice won most games")

if __name__ == "__main__":
    main()

