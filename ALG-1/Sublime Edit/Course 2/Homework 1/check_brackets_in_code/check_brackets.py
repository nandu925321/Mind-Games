# python3
from pathlib import Path
import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check(text):    
    opening_brackets_stack = []
    for index, char in enumerate(text, start=1):

        if char in ("[", "(", "{"):
            opening_brackets_stack.append(Bracket(char, index))

        elif char in ("]", ")", "}"):
            if not opening_brackets_stack:
                return index

            top = opening_brackets_stack.pop()
            if not top.Match(char):
                return index
    
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position

    return "Success"

if __name__ == "__main__":
    text = sys.stdin.read()
    print(check(text))

            


