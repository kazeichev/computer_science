from linked_list import LinkedList, Node


def sum_lists(ls1, ls2):
    if ls1.len() != ls2.len():
        return None

    node_1 = ls1.head
    node_2 = ls2.head
    result_list = LinkedList()

    while node_1 is not None and node_2 is not None:
        result_list.add_in_tail(Node(node_1.value + node_2.value))
        node_1 = node_1.next
        node_2 = node_2.next

    return result_list
