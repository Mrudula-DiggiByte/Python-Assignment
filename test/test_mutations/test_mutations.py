import unittest
from src.mutations.util import mutate_string  # Double-check if "scr" is typo; usually it’s "src"

class TestMutateString(unittest.TestCase):

    def test_basic_mutation(self):
        self.assertEqual(mutate_string("abracadabra", 5, "k"), "abrackdabra")

    def test_replace_first_character(self):
        self.assertEqual(mutate_string("hello", 0, "y"), "yello")

    def test_replace_last_character(self):
        self.assertEqual(mutate_string("hello", 4, "y"), "helly")

    def test_single_char_string(self):
        self.assertEqual(mutate_string("a", 0, "b"), "b")

    def test_no_change(self):
        self.assertEqual(mutate_string("hello", 1, "e"), "hello")  # same char

if __name__ == '__main__':
    unittest.main()
