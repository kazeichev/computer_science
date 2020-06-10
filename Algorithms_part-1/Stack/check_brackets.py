from stack import Stack


def check_brackets(string):
    stack = Stack()

    for i in list(string):
        if i == ')':
            if stack.size() == 0 or stack.pop() != '(':
                return False
        else:
            stack.push(i)

    if stack.size() == 0:
        return True
    else:
        return False
