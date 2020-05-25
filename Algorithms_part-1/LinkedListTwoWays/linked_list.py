class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node

            node = node.next

        return None

    def find_all(self, val):
        nodes = list()
        node = self.head

        while node is not None:
            if node.value == val:
                nodes.append(node)

            node = node.next

        return nodes

    def delete(self, val, all=False):
        current_node = self.head

        while current_node is not None:
            if current_node.value == val:
                if current_node.prev is None and current_node.next is not None:
                    self.head = current_node.next
                    self.head.prev = None
                elif current_node.prev is None and current_node.next is None:
                    self.head = None
                    self.tail = None
                elif self.tail == current_node:
                    self.tail = current_node.prev
                    self.tail.next = None
                else:
                    current_node.next.prev = current_node.prev
                    current_node.prev.next = current_node.next

                if all is False:
                    break

            current_node = current_node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length

    def insert(self, afterNode, newNode):
        current_node = self.head

        if afterNode is None:
            self.add_in_tail(newNode)
            return

        while current_node is not None:
            if current_node == afterNode:
                newNode.prev = current_node
                newNode.next = current_node.next

                if self.tail != current_node:
                    current_node.next.prev = newNode

                current_node.next = newNode

                if newNode.next is None:
                    self.tail = newNode

                break

            current_node = current_node.next

    def add_in_head(self, newNode):
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
