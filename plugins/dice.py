import random

from plugin import add_command

@add_command
def die(info, num="6"):
    return random.randint(1, int(num))

@add_command
def choose(info, *options):
    return random.choice(options)

@add_command
def coin(info):
    if random.random() >= .5:
        return "heads"
    else:
        return "tails"
