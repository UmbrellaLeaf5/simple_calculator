import re


class Stack:
    def __init__(self, items_list: list[str] = []):
        self.stack = items_list

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError("Stack is empty")
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def math_reset(self):
        self.stack = ["0"]

    def __setitem__(self, index, item):
        if index == len(self.stack) - 1 or index == -1:
            self.stack[index] = item
        else:
            raise IndexError("Invalid index")

    def __getitem__(self, index):
        if index == len(self.stack) - 1 or index == -1:
            return self.stack[index]
        else:
            raise IndexError("Invalid index")


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def remove_trailing_zeros(number: str):
    if "." in number:
        number = number.rstrip("0").rstrip(".")
    return number


def sci_round(expression: str):
    def convert(match):
        if len(match) > 16:
            return remove_trailing_zeros("{:e}".format(float(match)))
        return remove_trailing_zeros(match)

    pattern = r"\b[+-]?\d+\.\d+(?:[eE][+-]?\d+)?\b|\b\d+(?:[eE][+-]?\d+)?\b"
    converted_expression = re.sub(pattern, lambda match: convert(match.group()), expression)

    return converted_expression
