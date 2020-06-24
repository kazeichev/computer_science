import unittest
from native_dictionary import NativeDictionary


class PutToDictTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.d = NativeDictionary(19)

    def test(self):
        self.assertEqual(19, len(self.d))

        self.d.put("key_1", "value_1")
        self.d.put("key_2", "value_2")
        self.d.put("key_3", "value_3")

        self.assertEqual("value_1", self.d.get("key_1"))
        self.assertEqual("value_2", self.d.get("key_2"))
        self.assertEqual("value_3", self.d.get("key_3"))

        self.assertEqual(19, len(self.d))


class IsKeyExistTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.d = NativeDictionary(19)

    def test(self):
        self.assertFalse(self.d.is_key("key_1"))

        self.d.put("key_1", "value_1")
        self.assertTrue(self.d.is_key("key_1"))


if __name__ == '__main__':
    unittest.main()
