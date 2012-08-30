import random
from plugin import add_command

class Guesser():
    def __init__(self):
        self.reset()
    def reset(self):
        self.number = random.randint(0, 9)
    def guess(self, guess):
        is_correct = guess == self.number
        if is_correct:
            self.reset()
        return is_correct

guesser = Guesser()

@add_command
def guess(info, guess):
        """Guess a number from 0 to 9"""
        try:
            g = int(guess)
        except ValueError:
            return "Please read help"

        if guesser.guess(g):
            return "correct"
        else:
            return "incorrect"

