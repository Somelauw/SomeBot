import random
from plugin import add_command

class Guess():
    def __init__(self):
        self.reset()
    def reset(self):
        self.number = random.randint(0, 9)
    def guess(self, info, guess):
        is_correct = guess == self.number
        if is_correct:
            self.reset()
        return is_correct

guess = Guess()

@add_command
def guess(info, guess):
        """Guess a number from 0 to 9"""
        try:
            g = int(guess)
        except ValueError:
            return "Please read help"

        if guess.guess(g):
            return "correct"
        else:
            return "incorrect"

