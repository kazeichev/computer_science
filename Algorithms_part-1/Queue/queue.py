class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None

        element = self.queue[0]
        del self.queue[0]
        return element

    def size(self):
        return len(self.queue)
