from deque import Deque


def is_palindrom(string):
    deque = Deque()
    is_palindrom = False

    for i in list(string):
        deque.addTail(i)

    while deque.size() > 1:
        if deque.removeFront() == deque.removeTail():
            is_palindrom = True
        else:
            is_palindrom = False

    return is_palindrom
