class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        result = 0

        if v1 < v2:
            result = -1
        elif v1 > v2:
            result = +1

        return result

    def add(self, value):
        node = Node(value)
        current_node = self.head
        previous = None

        while current_node is not None:
            if self.compare(current_node.value, node.value) == (+1 if self.__ascending is True else -1):
                break

            previous, current_node = current_node, current_node.next

        if self.head is None:
            self.head = node
            self.tail = node
        elif previous is None:
            node.next, self.head.prev, self.head = self.head, node, node
        else:
            if previous == self.tail:
                self.tail = node

            node.next, node.prev, previous.next = current_node, previous, node

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            elif self.compare(node.value, val) == (+1 if self.__ascending is True else -1):
                return None

            node = node.next

        return None

    def delete(self, val):
        node = self.find(val)

        if node is None:
            return None

        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next

            if self.head is not None:
                self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev

            if self.tail is not None:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next

        return count

    def get_all(self):
        r = []
        node = self.head
        while node is not None:
            r.append(node)
            node = node.next
        return r


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        result = 0

        if v1.strip() < v2.strip():
            result = -1
        elif v1.strip() > v2.strip():
            result = +1

        return result
