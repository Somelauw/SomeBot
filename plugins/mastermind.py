from random import choice

from plugin import add_command

language = "0123456789"
code_length = 4

def random_code():
    return "".join(choice(language) for i in range(code_length))

def valid_guess(guess):
    return len(guess) == code_length and all(char in language for char in guess)

class Mastermind(object):
    def __init__(self):
        self.reset()

    def reset(self):
        self.code = random_code()

    def check_code(self, guess):
        """
        Compares the guess to the answer. If the answer is correct, it creates
        a new code. It returns feedback as a (correct, misplaced, errors)-
        tuple or None if the guess is invalid.
        """

        if valid_guess(guess):
            correct = sum(1 for (g, a) in zip(guess, self.code) if g == a)
            common = set(guess) & set(self.code)
            misplaced = sum(min([guess.count(c), self.code.count(c)]) 
                            for c in common) - correct
            #misplaced = sum(min([guess.count(s), self.code.count(s)]) 
                            #for s in set(self.code)) - correct
            errors = code_length - correct - misplaced
            return correct, misplaced, errors

game = Mastermind()

@add_command
def mastermind(info, guess):
    """Try to guess a mastermind code"""
    if valid_guess(guess):
        (c, m, e) = game.check_code(guess)
        if c == code_length:
            game.reset()
            return "Correct, %s" % info.user
        else:
            return "%d correct, %d misplaced and %d errors" % (c, m, e)
    else:   
        return "Invalid guess. Language is %s. Length is %d" %\
                (language, code_length)

