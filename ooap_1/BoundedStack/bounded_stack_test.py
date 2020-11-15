import unittest

from ooap_1.BoundedStack.bounded_stack import BoundedStack


class CreateBoundedStackWithoutArgsTestCase(unittest.TestCase):
    def test(self) -> None:
        stack = BoundedStack()

        self.assertIsInstance(stack, BoundedStack)
        self.assertEqual(stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)


class CreateBoundedStackWithArgsTestCase(unittest.TestCase):
    def test(self) -> None:
        stack = BoundedStack(10)

        self.assertIsInstance(stack, BoundedStack)
        self.assertEqual(stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)
        self.assertEqual(stack.get_max_size(), 10)


class PushToEmptyBoundedStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = BoundedStack(5)

    def test(self) -> None:
        self.assertIsInstance(self.stack, BoundedStack)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)

        self.assertIsNone(self.stack.push(1))
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_OK)
        self.assertEqual(self.stack.size(), 1)


class PushToNotEmptyBoundedStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = BoundedStack(2)

    def test(self) -> None:
        self.assertIsInstance(self.stack, BoundedStack)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)

        self.stack.push(1)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_OK)
        self.assertEqual(self.stack.size(), 1)

        self.stack.push(2)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_OK)
        self.assertEqual(self.stack.size(), 2)

        self.stack.push(3)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_ERR)
        self.assertEqual(self.stack.size(), 2)


class PopFromEmptyBoundedStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = BoundedStack()

    def test(self) -> None:
        self.assertIsInstance(self.stack, BoundedStack)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)
        self.assertEqual(self.stack.size(), 0)

        self.stack.pop()

        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_ERR)
        self.assertEqual(self.stack.size(), 0)


class PopFromNotEmptyBoundedStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = BoundedStack(5)

    def test(self) -> None:
        self.assertIsInstance(self.stack, BoundedStack)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)
        self.assertEqual(self.stack.size(), 0)

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.size(), 3)

        self.stack.pop()

        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_OK)
        self.assertEqual(self.stack.size(), 2)


class PeekFromEmptyBoundedStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = BoundedStack(5)

    def test(self) -> None:
        self.assertIsInstance(self.stack, BoundedStack)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)
        self.assertEqual(self.stack.size(), 0)

        self.assertEqual(self.stack.peek(), 0)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_ERR)


class PeekFromNotEmptyBoundedStackTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.stack = BoundedStack(5)

    def test(self) -> None:
        self.assertIsInstance(self.stack, BoundedStack)
        self.assertEqual(self.stack.get_push_status(), BoundedStack.STATUS_PUSH_NIL)
        self.assertEqual(self.stack.get_pop_status(), BoundedStack.STATUS_POP_NIL)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_NIL)
        self.assertEqual(self.stack.size(), 0)

        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        self.assertEqual(self.stack.size(), 3)

        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.get_peek_status(), BoundedStack.STATUS_PEEK_OK)


if __name__ == '__main__':
    unittest.main()
