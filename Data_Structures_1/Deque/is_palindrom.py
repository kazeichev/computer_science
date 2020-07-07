from deque import Deque


def is_palindrom(string):
    deque = Deque()

    for i in list(string):
        deque.addTail(i)

    while deque.size() > 1:
        if deque.removeFront() != deque.removeTail():
            return False

    return True
