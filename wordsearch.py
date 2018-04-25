

class WordSearch(object):

    ROW_LENGTH = 4

    def __init__(self, grid):
        self.grid = grid
        self.grid_lookup = {}

        for index, letter in enumerate(grid):
            if letter not in self.grid_lookup:
                self.grid_lookup[letter] = [index]
            else:
                self.grid_lookup[letter].append(index)

    def is_present(self, word):
        if word and word[0] in self.grid_lookup:
            for index in self.grid_lookup[word[0]]:
                if self._check_row(index, word) or \
                        self._check_column(index, word):
                    return True

    def _check_row(self, index, word):
        row_position = index % WordSearch.ROW_LENGTH
        return self._check_word(index, word, 1, row_position)

    def _check_column(self, index, word):
        column_position = index / WordSearch.ROW_LENGTH
        return self._check_word(
            index, word, WordSearch.ROW_LENGTH, column_position)

    def _check_word(self, index, word, increment, test):
        for i, letter in enumerate(word):
            if test is WordSearch.ROW_LENGTH or letter is not self.grid[index]:
                return False
            index += increment
            test += 1
        return True


if __name__ == '__main__':

    grid = 'abcdjejddedeeaee'

    words = [
        'abc',
        'eeee',
        'jej',
        'ajd',
        'cdj'
    ]

    ws = WordSearch(grid)

    for word in words:
        if ws.is_present(word):
            print 'found: {}'.format(word)
