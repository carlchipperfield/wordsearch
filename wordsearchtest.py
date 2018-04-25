import unittest
from wordsearch import WordSearch


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        grid = 'abcd' \
               'efgh' \
               'ijee' \
               'kfkr'
        cls.ws = WordSearch(grid)

    def test_empty_word(self):
        self.assertFalse(self.ws.is_present(''))

    def test_not_present(self):
        self.assertFalse(self.ws.is_present('hhh'))

    def test_basic_row_present(self):
        self.assertTrue(self.ws.is_present('abc'))

    def test_basic_column_present(self):
        self.assertTrue(self.ws.is_present('dhe'))

    def test_row_max(self):
        self.assertTrue(self.ws.is_present('efgh'))

    def test_column_max(self):
        self.assertTrue(self.ws.is_present('ijee'))

    def test_longer_than_row(self):
        self.assertFalse(self.ws.is_present('efghaa'))

    def test_longer_than_column(self):
        self.assertFalse(self.ws.is_present('ijeeej'))

    def test_word_wraps_row(self):
        self.assertFalse(self.ws.is_present('cdef'))

if __name__ == '__main__':
    unittest.main()
