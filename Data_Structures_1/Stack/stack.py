class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None

        last_element = self.stack[self.size() - 1]
        self.stack = self.stack[:-1]
        return last_element

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None

        return self.stack[self.size() - 1]
