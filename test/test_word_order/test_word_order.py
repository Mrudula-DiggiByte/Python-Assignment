import unittest
from src.word_order.util import count_words

class TestCountWords(unittest.TestCase):

    def test_all_unique_words(self):
        words = ["apple", "banana", "cherry"]
        expected_unique = 3
        expected_freq = "1 1 1"
        unique, freq = count_words(words)
        self.assertEqual(unique, expected_unique)
        self.assertEqual(freq, expected_freq)

    def test_some_repeating_words(self):
        words = ["apple", "banana", "apple", "apple", "banana", "grape"]
        expected_unique = 3
        expected_freq = "3 2 1"
        unique, freq = count_words(words)
        self.assertEqual(unique, expected_unique)
        self.assertEqual(freq, expected_freq)

    def test_one_word_multiple_times(self):
        words = ["hello"] * 5
        expected_unique = 1
        expected_freq = "5"
        unique, freq = count_words(words)
        self.assertEqual(unique, expected_unique)
        self.assertEqual(freq, expected_freq)

    def test_empty_list(self):
        words = []
        expected_unique = 0
        expected_freq = ""
        unique, freq = count_words(words)
        self.assertEqual(unique, expected_unique)
        self.assertEqual(freq, expected_freq)

    def test_case_sensitivity(self):
        words = ["Hello", "hello", "HELLO"]
        expected_unique = 3
        expected_freq = "1 1 1"
        unique, freq = count_words(words)
        self.assertEqual(unique, expected_unique)
        self.assertEqual(freq, expected_freq)

if __name__ == '__main__':
    unittest.main()
