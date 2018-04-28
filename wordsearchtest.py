import unittest
from wordsearch import WordSearch


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        grid = 'abcdj' \
               'efghm' \
               'ijeen' \
               'kfkrj' \
               'kfkbc'
        cls.ws = WordSearch(grid, row_length=5)

    def test_empty_word(self):
        self.assertFalse(self.ws.is_present(''))

    def test_not_present(self):
        self.assertFalse(self.ws.is_present('hhh'))

    def test_basic_row_present(self):
        self.assertTrue(self.ws.is_present('abc'))

    def test_basic_column_present(self):
        self.assertTrue(self.ws.is_present('dhe'))

    def test_row_max(self):
        self.assertTrue(self.ws.is_present('efghm'))

    def test_column_max(self):
        self.assertTrue(self.ws.is_present('bfjff'))

    def test_longer_than_row(self):
        self.assertFalse(self.ws.is_present('efghmaa'))

    def test_longer_than_column(self):
        self.assertFalse(self.ws.is_present('bfjffjj'))

    def test_word_wraps_row(self):
        self.assertFalse(self.ws.is_present('cdjef'))


if __name__ == '__main__':
    unittest.main()
