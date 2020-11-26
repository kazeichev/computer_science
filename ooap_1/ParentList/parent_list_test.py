import unittest
from ooap_1.ParentList.parent_list import LinkedList, Node, TwoWayList


class HeadLinkedList(unittest.TestCase):
    def test(self):
        l = LinkedList()
        self.assertEqual(l.get_list_head_status(), LinkedList.STATUS_NIL)

        l.head()
        self.assertEqual(l.get_list_head_status(), LinkedList.STATUS_ERR)

        node_1 = Node(1)

        l.add_tail(node_1)
        self.assertEqual(l.get_add_tail_status(), LinkedList.STATUS_OK)

        l.head()
        self.assertEqual(l.get_list_head_status(), LinkedList.STATUS_OK)

        self.assertEqual(l.get_get_status(), LinkedList.STATUS_NIL)
        self.assertEqual(l.get(), node_1.value)
        self.assertEqual(l.get_get_status(), LinkedList.STATUS_OK)

        self.assertTrue(l.is_head())
        self.assertTrue(l.is_tail())

        self.assertEqual(l.size(), 1)


class FindLinkedList(unittest.TestCase):
    def test(self):
        l = LinkedList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(2)
        node_5 = Node(1)

        l.add_tail(node_1)
        l.add_tail(node_2)
        l.add_tail(node_3)
        l.add_tail(node_4)
        l.add_tail(node_5)

        l.head()
        l.find(2)
        self.assertEqual(l.get(), node_4.value)

        l.find(2)
        self.assertEqual(l.get(), node_2.value)
        self.assertEqual(l.size(), 5)


class LeftLinkedList(unittest.TestCase):
    def test(self):
        l = TwoWayList()
        node_1 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)
        node_4 = Node(4)
        node_5 = Node(5)

        l.add_tail(node_1)
        l.add_tail(node_2)
        l.add_tail(node_3)
        l.add_tail(node_4)
        l.add_tail(node_5)

        l.tail()
        l.left()
        l.left()

        self.assertEqual(l.get(), 3)

        l.left()
        l.left()
        l.left()

        self.assertEqual(l.get_left_status(), TwoWayList.STATUS_ERR)

        l.clear()
        self.assertFalse(l.is_value())
