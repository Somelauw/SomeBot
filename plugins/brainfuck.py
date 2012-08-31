import io
from collections import defaultdict
from sys import stdin, stdout, argv
from string import digits, atoi

from plugin import add_command

# http://pytute.blogspot.nl/2007/04/python-plugin-system.html


def jumptable(src):
   table = {}
   stack = []
   for index, char in enumerate(src):
       if char == "[":
           stack.append(index)
       elif char == "]":
           index2 = stack.pop()
           table[index] = index2
           table[index2] = index
   return table

#def strip_comments(src):
    #return "".join(char for char in src if char in "+-[]<>,.")

class Brainfuck(object):
    def __init__(self, source, stdin=None, stdout=None):
        self.source = source
	self.jumptable = jumptable(self.source)
	self.stdin = stdin or sys.stdin
	self.stdout = stdout or sys.stdout

        self.tape = defaultdict(lambda: 0)
	self.pointer = 0
        self.program = 0

    def run(self):
        while self.is_running():
	    self.step()

    def is_running(self):
        return self.program < len(self.source)

    def step(self):
	c = self.source[self.program]
        if c == ",":
            self.tape[self.pointer] = ord(self.stdin.read(1) or "\0")
        elif c == ".":
            self.stdout.write(chr(self.tape[self.pointer]))
        elif c == "+":
            self.tape[self.pointer] += 1
        elif c == "-":
            self.tape[self.pointer] -= 1
        elif c == ">":
            self.pointer += 1
        elif c == "<":
            self.pointer -= 1
        elif c == "[" and not self.tape[self.pointer]:
	    self.program = self.jumptable[self.program]
        elif c == "]" and self.tape[self.pointer]:
	    self.program = self.jumptable[self.program]

	self.program += 1

@add_command
def brainfuck(info, src):
    """Executes a brainfuck program"""
    stdin = io.BytesIO(
            "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod")
    stdout = io.BytesIO()

    # Keep running under very strict conditions
    steps = 0
    interpreter = Brainfuck(src, stdin, stdout)
    while interpreter.is_running() and stdout.tell() < 100 and steps < 500:
        interpreter.step()
        steps += 1

    return stdout.getvalue()

