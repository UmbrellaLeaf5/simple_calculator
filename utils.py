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
