import random


def roll_dice():
    """Roll two dice and return both values and their sum."""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    print(f"The sum of dice is {die1} + {die2} = {total}")
    return total

def first_roll():
    
    total = roll_dice()

    # Winning numbers 
    if total in [7, 11]:
        print("You won")
        return None

    # Losing numbers
    elif total in [2, 3, 12]:
        print("You lose")
        return None

    else:
        print(f"Now your goal number is {total}")
        return total

def keep_rolling(goal):
    """Keep rolling until player hits goal number (win) or rolls 7 (lose)."""
    while True:
        total = roll_dice()

        if total == goal:
            print("You won")
            break
        elif total == 7:
            print("You lose")
            break

def play_game():
    """Play one full round of Craps."""
    goal = first_roll()

    # The game didn't end on the first roll
    if goal is not None:
        keep_rolling(goal)


play_game()