

class Grid(object):

    def __init__(self, grid, row_length):
        self.grid = grid
        self.row_length = row_length

    def get_letter_data(self, length):
        for index, letter in enumerate(self.grid):
            yield index, letter, self._get_letters_row(index, length), \
                    self._get_letters_column(index, length)

    def _get_letters_row(self, start_index, length):
        end_index = start_index + length
        row_end = start_index - (start_index % self.row_length) + self.row_length
        if row_end > end_index:
            return self.grid[start_index:end_index]
        else:
            return self.grid[start_index:row_end]

    def _get_letters_column(self, start_index, length):
        return self.grid[start_index:self.row_length * length:self.row_length]

    def is_present_in_row(self, start_index, word):
        row_end = start_index - (start_index % self.row_length) + self.row_length
        return self._check_grid(start_index, word, increment=1, boundary=row_end)

    def is_present_in_column(self, start_index, word):
        return self._check_grid(
            start_index, word, increment=self.row_length, boundary=len(self.grid))

    def _check_grid(self, index, word, increment, boundary):
        for letter in word:
            if index >= boundary or not self.grid[index] == letter:
                return False
            index += increment
        else:
            return True


class GridLookup(object):
    """
        Responsible for indexing a grid for faster lookups of a word, either by checking for an exact match or
        retrieving a list of possible positions in the grid for longer words.

        The grid is stored as a tree, using dictionaries. Each letter is indexed along with the next x letters
        that appear horizontally and vertically, x being defined as max_word_length. If the length of the sequence of
        letters indexed is equal to max_word_length then the position of the letter is added to a list.

        An example:
            A -> N -> E -> [2]
              -> N -> I -> [1, 4, 5]
              -> C
            B -> E
    """
    def __init__(self, grid, max_word_length):
        self.grid_lookup = {}
        self.max_word_length = max_word_length

        for index, _, row, col in grid.get_letter_data(max_word_length):
            self._index_grid_sequence(index, row)
            self._index_grid_sequence(index, col)

    def is_present(self, word):
        if not word:
            return False
        try:
            node = self.grid_lookup
            for letter in word:
                node = node[letter]
        except KeyError:
            return False
        else:
            return True

    def get_grid_indexes(self, word):
        try:
            node = self.grid_lookup
            for letter in word[0:self.max_word_length]:
                node = node[letter]
        except (KeyError, IndexError):
            return []
        else:
            if isinstance(node, list):
                return node
            else:
                return []

    def _index_grid_sequence(self, grid_index, sequence):
        node = self.grid_lookup
        for index, item in enumerate(sequence):
            if item not in node:
                if index < self.max_word_length - 1:
                    node[item] = {}
                else:
                    node[item] = [grid_index]
            else:
                if index == self.max_word_length - 1:
                    node[item].append(grid_index)
            node = node[item]
