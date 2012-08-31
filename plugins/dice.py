import random

from plugin import add_command

@add_command
def die(info, num="6"):
    """Returns a number below 6 or another limit"""

    return random.randint(1, int(num))

@add_command
def choose(info, *options):
    """Make a choice between the offered options"""

    return random.choice(options)

@add_command
def coin(info):
    """Simply flip a coin"""

    if random.random() >= .5:
        return "heads"
    else:
        return "tails"
