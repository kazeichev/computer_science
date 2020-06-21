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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            return

        if self.__ascending:
            current_node = self.head
            prev_node = None
            is_break = True

            while is_break and current_node is not None:
                if self.compare(value, current_node.value) == 1:
                    current_node, prev_node = current_node.next, current_node
                else:
                    is_break = False

            if current_node is None:
                self.tail = new_node
                self.tail.prev, prev_node.next = prev_node, self.tail
            else:
                if current_node is self.head:
                    current_node.prev = new_node
                    current_node.prev.next, self.head = self.head, current_node.prev
                else:
                    current_node.prev = new_node
                    prev_node.next = current_node.prev
                    current_node.prev.prev, current_node.prev.next = prev_node, current_node
        else:
            current_node = self.tail
            prev_node = None
            is_break = True

            while is_break and current_node is not None:
                if self.compare(value, current_node.value) != -1:
                    current_node, prev_node = current_node.prev, current_node
                else:
                    is_break = False

            if current_node is None:
                self.head = new_node
                self.head.next, prev_node.prev = prev_node, self.head
            else:
                if current_node is self.tail:
                    current_node.next = new_node
                    current_node.next.prev, self.tail = self.tail, current_node.next
                else:
                    current_node.next = new_node
                    prev_node.prev = current_node.next
                    current_node.next.next, current_node.next.prev = prev_node, current_node

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

    def len_reverse(self):
        count = 0
        node = self.tail

        while node is not None:
            count += 1
            node = node.prev

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
