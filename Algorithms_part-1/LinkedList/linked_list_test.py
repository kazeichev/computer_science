from linked_list import LinkedList, Node


def create_list(node_names):
    linked_list = LinkedList()
    for i in node_names.values():
        linked_list.add_in_tail(Node(i))

    return linked_list


def create_node():
    node_1 = Node(0)
    if node_1.value != 0:
        raise ValueError("Node val == 0 : {}".format(node_1.value))

    node_2 = Node("")
    if node_2.value != "":
        raise ValueError("Node val == '' : {}".format(node_2.value))

    node_1.next = node_2
    if node_1.next != node_2:
        raise ValueError("Node next == node_2 : {}".format(node_1.next))

    print('Create node: success')


def add_in_tail():
    linked_list = LinkedList()

    if linked_list.head is not None or linked_list.tail is not None:
        raise ValueError("Linked list created : head - {} tail - {}".format(linked_list.head, linked_list.tail))

    node_1 = Node(1)
    linked_list.add_in_tail(node_1)

    if linked_list.head != node_1:
        raise ValueError("LinkedList head == node_1 : {}".format(linked_list.head))

    if linked_list.tail != node_1:
        raise ValueError("LinkedList tail == node_1 : {}".format(linked_list.tail))

    print('Add in tail: success')


def clean():
    """
        Очистка списка
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3
    })
    ls.clean()

    if ls.head is not None or ls.tail is not None:
        raise ValueError("Очистка списка. ls.head is not None: {}, ls.tail is not None: {}".format(ls.head, ls.tail))

    print("Clean: success")


def delete():
    """
        Удалить один первый элемент
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3
    })
    ls.delete(1, False)
    if ls.head.value != 2:
        raise ValueError("Удалить один первый элемент. ls.head.value != 2 : {}".format(ls.head.value))

    if ls.head.next.value != 3:
        raise ValueError("Удалить один первый элемент. ls.head.next.value != 3 : {}".format(ls.head.next.value))

    """
        Удалить первый элемент, если все значения одинаковы
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 1,
        'name_3': 1
    })
    ls.delete(1, False)
    if ls.head.value != 1:
        raise ValueError(
            "Удалить первый элемент, если все значения одинаковы. ls.head.value != 1 : {}"
            .format(ls.head.value)
        )

    if ls.len() != 2:
        raise ValueError(
            "Удалить первый элемент, если все значения одинаковы. ls.len() != 2 : {}"
            .format(ls.len())
        )

    """
        Удалить два первых элемента
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 1,
        'name_3': 2,
        'name_4': 3
    })
    ls.delete(1, True)
    if ls.head.value != 2:
        raise ValueError("Удалить два первых элемента. ls.head.value != 2 : {}".format(ls.head.value))

    if ls.head.next.value != 3:
        raise ValueError("Удалить два первых элемента. ls.head.next.value != 3 : {}".format(ls.head.next.value))

    """
        Удалить первый и последний элементы
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3,
        'name_4': 1
    })
    ls.delete(1, True)
    if ls.head.value != 2:
        raise ValueError("Удалить первый и последний элементы. ls.head.value != 2 : {}".format(ls.head.value))

    if ls.head.next.value != 3:
        raise ValueError("Удалить первый и последний элементы. ls.head.next.value != 3 : {}".format(ls.head.next.value))

    if ls.tail.value != 3 or ls.tail.next is not None:
        raise ValueError(
            "Удалить первый элемент. ls.tail.value != 3: {}, ls.tail.next is not None : {}"
                .format(ls.tail.value, ls.tail.next))

    """
        Удалить последний элемент
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3,
        'name_4': 4
    })
    ls.delete(4, False)
    if ls.tail.next is not None:
        raise ValueError("Удалить последний элемент. ls.tail.next is not None : {}".format(ls.tail.next))

    if ls.tail.value != 3:
        raise ValueError("Удалить последний элемент. ls.tail.value != 3 : {}".format(ls.tail.value))

    """
        Удалить два последних элемента
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3,
        'name_4': 4,
        'name_5': 4,
    })
    ls.delete(4, True)
    if ls.tail.value != 3 or ls.tail.next is not None:
        raise ValueError(
            "Удалить два последних элемента. ls.tail.value != 3: {}, ls.tail.next is not None: {}"
                .format(ls.tail.value, ls.tail.next)
        )

    """
        Удалить элемент в середине
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3,
        'name_4': 4
    })
    ls.delete(2, False)
    if ls.find(1).next.value != 3:
        raise ValueError(
            "Удалить элемент в середине. ls.find(1).next.value != 3 : {}"
            .format(ls.find(1).next.value)
        )

    """
        Удалить два элемента в середине
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 3,
        'name_4': 3,
        'name_5': 4
    })
    ls.delete(3, True)
    if ls.find(2).next.value != 4:
        raise ValueError(
            "Удалить два элемента в середине. ls.find(1).next.value != 3 : {}"
                .format(ls.find(2).next.value)
        )

    """
        Список пустой
    """
    ls = LinkedList()
    ls.delete(1)

    """
        Один элемент в списке
    """
    ls = LinkedList()
    ls.add_in_tail(Node(1))
    ls.delete(1)
    if ls.head is not None or ls.tail is not None:
        raise ValueError("Один элемент в списке. head == None: {}, tail == None: {}".format(ls.head, ls.tail))

    print('Delete: success')


def find_all():
    """
        Поиск всех элементов
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 1,
        'name_4': '1',
        'name_5': '6',
        'name_6': 6,
    })
    nodes = ls.find_all(1)
    if len(nodes) != 2:
        raise ValueError("Поиск всех элементов. len(nodes) != 2: {}".format(len(nodes)))

    if nodes[0].value != 1 or nodes[1].value != 1:
        raise ValueError(
            "Поиск всех элементов. nodes[0].value != 1: {}, nodes[1].value != 1: {}"
                .format(nodes[0].value, nodes[1].value)
        )

    print("Find all: success")


def length():
    """
        Длинна списка c элементами
    """
    ls = create_list({
        'name_1': 1,
        'name_2': 2,
        'name_3': 1,
        'name_4': '1',
        'name_5': '6',
        'name_6': 6,
    })
    count = ls.len()
    if count != 6:
        raise ValueError("Длинна списка c элементами. count != 6: {}".format(count))

    """
        Длинна пустого списка
    """
    ls = create_list({})
    count = ls.len()
    if count != 0:
        raise ValueError("Длинна списка c элементами. count != 0: {}".format(count))

    print("Length: success")


def insert():
    """
        Вставка после первого элемента
    """
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_test = Node('test')
    ls = LinkedList()
    ls.add_in_tail(node_1)
    ls.add_in_tail(node_2)
    ls.add_in_tail(node_3)
    ls.insert(node_1, node_test)

    if node_1.next != node_test:
        raise ValueError("Вставка после первого элемента. node_1.next != node_tes: {}".format(node_1.next))

    """
        Вставка по середине
    """
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_test = Node('test')
    ls = LinkedList()
    ls.add_in_tail(node_1)
    ls.add_in_tail(node_2)
    ls.add_in_tail(node_3)
    ls.insert(node_2, node_test)

    if node_2.next != node_test:
        raise ValueError("Вставка по середине. node_2.next != node_tes: {}".format(node_2.next))

    """
        Вставка в конце
    """
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_test = Node('test')
    ls = LinkedList()
    ls.add_in_tail(node_1)
    ls.add_in_tail(node_2)
    ls.add_in_tail(node_3)
    ls.insert(node_3, node_test)

    if node_3.next != node_test:
        raise ValueError("Вставка в конце. node_3.next != node_test: {}".format(node_3.next))

    if node_test.next is not None:
        raise ValueError("Вставка в конце. node_test.next is not None: {}".format(node_test.next))

    print("Insert: success")


def linked_list_test():
    create_node()
    add_in_tail()
    delete()
    clean()
    find_all()
    length()
    insert()


linked_list_test()
