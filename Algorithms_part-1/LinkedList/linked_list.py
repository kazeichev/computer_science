class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        prev_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.value == val:
                if prev_node is None and self.tail != current_node:
                    self.head = current_node.next
                    current_node = current_node.next
                    if all is False:
                        break
                    continue
                elif prev_node is None and self.tail == current_node:
                    self.head = None
                    self.tail = None
                elif self.tail == current_node:
                    self.tail = prev_node
                    self.tail.next = None
                else:
                    prev_node.next = current_node.next
                    current_node = current_node.next
                    if all is False:
                        break
                    continue

                if all is False:
                    break

            prev_node = current_node
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

        while current_node is not None:
            if current_node == afterNode:
                newNode.next = current_node.next
                current_node.next = newNode

            current_node = current_node.next
