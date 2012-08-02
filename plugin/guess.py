import random
from plugin import add_command

class Guess():
    def __init__(self):
        self.reset()
    def reset(self):
        self.number = random.randint(0, 9)
    def guess(self, info, guess):
        """Guess a number from 0 to 9"""

        try:
            g = int(guess)
        except ValueError:
            return "Please read help"

        if g == self.number:
            self.reset()
            return "correct"
        else:
            return "incorrect"

guess = Guess()
add_command(guess.guess)
