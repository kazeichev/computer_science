from linked_list import LinkedList2, Node

import unittest


class FindFirstElementTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)

    def test_find_in_empty(self):
        self.assertEqual(self.ls.find(1), None)
        self.assertEqual(self.ls.head, None)
        self.assertEqual(self.ls.tail, None)

    def test_find_in_list_with_single_node(self):
        self.ls.add_in_tail(self.node_1)

        self.assertEqual(self.ls.find(1), self.node_1)
        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_1)

    def test_find_in_list_of_equal_nodes(self):
        node_2 = Node(1)
        node_3 = Node(1)

        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(node_2)
        self.ls.add_in_tail(node_3)

        self.assertEqual(self.ls.find(1), self.node_1)
        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, node_3)

    def test_find_in_simple_list(self):
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_2)
        self.ls.add_in_tail(self.node_3)

        self.assertEqual(self.ls.find(2), self.node_2)
        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_3)


class FindAllElementsTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)

    def test_find_in_empty_list(self):
        self.assertEqual(self.ls.find_all(1), [])
        self.assertIsNone(self.ls.head)
        self.assertIsNone(self.ls.tail)

    def test_find_in_list_with_single_node(self):
        self.ls.add_in_tail(self.node_1)

        self.assertEqual(self.ls.find_all(1), [self.node_1])
        self.assertNotEqual(self.ls.find_all(2), [self.node_1])
        self.assertEqual(self.ls.find_all(3), [])
        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_1)


class DeleteSingleElementTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)

    def generate_list(self):
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_2)
        self.ls.add_in_tail(self.node_3)

    def test_delete_from_empty_list(self):
        self.ls.delete(1, False)
        self.assertIsNone(self.ls.head)
        self.assertIsNone(self.ls.tail)

    def test_delete_from_list_with_single_node(self):
        self.ls.add_in_tail(self.node_1)
        self.ls.delete(1, False)

        self.assertIsNone(self.ls.head)
        self.assertIsNone(self.ls.tail)

    def test_delete_first_node(self):
        self.generate_list()
        self.ls.delete(1, False)

        self.assertEqual(self.ls.head, self.node_2)
        self.assertIsNone(self.node_2.prev)
        self.assertEqual(self.ls.head.next, self.node_3)
        self.assertEqual(self.ls.tail.prev, self.node_2)
        self.assertEqual(self.ls.tail, self.node_3)

    def test_delete_middle_node(self):
        self.generate_list()
        self.ls.delete(2, False)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.head.next, self.node_3)
        self.assertEqual(self.ls.tail.prev, self.node_1)
        self.assertEqual(self.ls.tail, self.node_3)

    def test_delete_last_node(self):
        self.generate_list()
        self.ls.delete(3, False)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.head.next, self.node_2)
        self.assertEqual(self.ls.tail.prev, self.node_1)
        self.assertEqual(self.ls.tail, self.node_2)
        self.assertIsNone(self.ls.tail.next)

    def test_delete_first_node_if_all_values_equal(self):
        node_test_1 = Node(1)
        node_test_2 = Node(1)

        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(node_test_1)
        self.ls.add_in_tail(node_test_2)
        self.ls.delete(1, False)

        self.assertEqual(self.ls.head, node_test_1)
        self.assertEqual(self.ls.head.next, node_test_2)
        self.assertEqual(self.ls.tail.prev, node_test_1)
        self.assertEqual(self.ls.tail, node_test_2)


class DeleteMultipleElementsTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1_1 = Node(1)
        self.node_1_2 = Node(1)
        self.node_2_1 = Node(2)
        self.node_2_2 = Node(2)
        self.node_3_1 = Node(3)
        self.node_3_2 = Node(3)

        self.ls.add_in_tail(self.node_1_1)
        self.ls.add_in_tail(self.node_1_2)
        self.ls.add_in_tail(self.node_2_1)
        self.ls.add_in_tail(self.node_2_2)
        self.ls.add_in_tail(self.node_3_1)
        self.ls.add_in_tail(self.node_3_2)

    def test_delete_two_first_equal_values(self):
        self.ls.delete(1, True)

        self.assertEqual(self.ls.head, self.node_2_1)
        self.assertIsNone(self.node_2_1.prev)
        self.assertEqual(self.node_2_1.next, self.node_2_2)
        self.assertEqual(self.ls.tail, self.node_3_2)
        self.assertEqual(self.ls.tail.prev, self.node_3_1)

    def test_delete_two_last_equal_values(self):
        self.ls.delete(3, True)

        self.assertEqual(self.ls.tail, self.node_2_2)
        self.assertIsNone(self.ls.tail.next)
        self.assertEqual(self.ls.tail.prev, self.node_2_1)
        self.assertEqual(self.ls.head, self.node_1_1)

    def test_delete_two_middle_equal_values(self):
        self.ls.delete(2, True)

        self.assertEqual(self.ls.head, self.node_1_1)
        self.assertEqual(self.ls.tail, self.node_3_2)
        self.assertIsNone(self.ls.tail.next)
        self.assertEqual(self.node_1_2.next, self.node_3_1)
        self.assertEqual(self.node_3_1.prev, self.node_1_2)

    def test_delete_first_middle_last_values(self):
        self.ls = LinkedList2()
        node_1_1 = Node(1)
        node_1_2 = Node(1)
        node_1_3 = Node(1)
        node_2 = Node(2)
        node_3 = Node(3)

        self.ls.add_in_tail(node_1_1)
        self.ls.add_in_tail(node_2)
        self.ls.add_in_tail(node_1_2)
        self.ls.add_in_tail(node_3)
        self.ls.add_in_tail(node_1_3)

        self.ls.delete(1, True)

        self.assertEqual(self.ls.head, node_2)
        self.assertIsNone(self.ls.head.prev)
        self.assertEqual(self.ls.head.next, node_3)
        self.assertEqual(node_3.prev, node_2)
        self.assertEqual(self.ls.tail, node_3)
        self.assertIsNone(self.ls.tail.next)


class InsertElementTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)

    def test_after_is_none_and_list_empty(self):
        self.ls.insert(None, self.node_1)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_1)
        self.assertIsNone(self.ls.head.prev)
        self.assertIsNone(self.ls.tail.next)

    def test_after_is_none_and_list_not_empty(self):
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_2)

        self.ls.insert(None, self.node_3)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_3)
        self.assertEqual(self.ls.tail.prev, self.node_2)
        self.assertEqual(self.ls.head.next, self.node_2)
        self.assertIsNone(self.ls.tail.next)
        self.assertIsNone(self.ls.head.prev)

    def test_insert_in_middle(self):
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_3)

        self.ls.insert(self.node_1, self.node_2)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_3)
        self.assertEqual(self.ls.head.next, self.node_2)
        self.assertEqual(self.ls.tail.prev, self.node_2)
        self.assertEqual(self.node_2.next, self.node_3)
        self.assertEqual(self.node_2.prev, self.node_1)
        self.assertIsNone(self.ls.tail.next)
        self.assertIsNone(self.ls.head.prev)

    def test_insert_in_tail(self):
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_2)

        self.ls.insert(self.node_2, self.node_3)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_3)
        self.assertEqual(self.node_2.next, self.node_3)
        self.assertEqual(self.node_3.prev, self.node_2)
        self.assertIsNone(self.ls.tail.next)
        self.assertIsNone(self.ls.head.prev)


class AddInHeadTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)
        self.ls.add_in_tail(self.node_2)
        self.ls.add_in_tail(self.node_3)

    def test_add_in_head_of_empty_list(self):
        self.ls = LinkedList2()
        self.ls.add_in_head(self.node_1)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertIsNone(self.ls.head.prev)
        self.assertIsNone(self.ls.head.next)
        self.assertEqual(self.ls.tail, self.node_1)
        self.assertIsNone(self.ls.tail.next)

    def test_add_in_head_of_list_with_single_element(self):
        self.ls = LinkedList2()
        self.ls.add_in_tail(self.node_2)
        self.ls.add_in_head(self.node_1)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertEqual(self.ls.tail, self.node_2)
        self.assertEqual(self.ls.head.next, self.node_2)
        self.assertEqual(self.ls.tail.prev, self.node_1)
        self.assertIsNone(self.ls.head.prev)
        self.assertIsNone(self.ls.tail.next)

    def test_add_in_head_of_not_empty_list(self):
        self.ls.add_in_head(self.node_1)

        self.assertEqual(self.ls.head, self.node_1)
        self.assertIsNone(self.ls.head.prev)
        self.assertEqual(self.ls.head.next, self.node_2)
        self.assertEqual(self.node_2.prev, self.node_1)
        self.assertEqual(self.node_2.next, self.node_3)
        self.assertEqual(self.ls.tail, self.node_3)
        self.assertEqual(self.ls.tail.prev, self.node_2)


class CleanTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_2)
        self.ls.add_in_tail(self.node_3)

    def test_clean_empty_list(self):
        self.ls = LinkedList2()
        self.ls.clean()

        self.assertIsNone(self.ls.head)
        self.assertIsNone(self.ls.tail)

    def test_clean_list(self):
        self.ls.clean()

        self.assertIsNone(self.ls.head)
        self.assertIsNone(self.ls.tail)


class LenTestCase(unittest.TestCase):
    def setUp(self):
        self.ls = LinkedList2()
        self.node_1 = Node(1)
        self.node_2 = Node(2)
        self.node_3 = Node(3)
        self.ls.add_in_tail(self.node_1)
        self.ls.add_in_tail(self.node_2)
        self.ls.add_in_tail(self.node_3)

    def test_length_of_empty_list(self):
        self.ls = LinkedList2()
        length = self.ls.len()

        self.assertEqual(length, 0)

    def test_length(self):
        length = self.ls.len()

        self.assertEqual(length, 3)


if __name__ == '__main__':
    unittest.main()
