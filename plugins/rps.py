import random

from plugin import add_command

moves = "rps"

move_names = {
        "r": "rock",
        "p": "paper",
        "s": "scissors"
        }

def rps_winner(move):
    return moves[(moves.index(move) + 1) % len(moves)]

@add_command
def rps(info, choice):
    """(R)ock, (P)aper, (S)cissors"""

    choice = (choice or " ")[0].lower()
    choice2 = random.choice(moves)

    if choice not in moves:
        print "invalid", choice
        return "Not a valid move"
    elif choice == choice2:
        return "Draw"
    elif choice == rps_winner(choice2):
        return "You win from %s" % move_names[choice2]
    else:
        return "You lost from %s" % move_names[choice2]
    
