from grid import Grid, GridLookup

ROW_LENGTH = 10000
INDEX_LENGTH = 4


class WordSearch(object):

    def __init__(self, grid, row_length=ROW_LENGTH, index_length=INDEX_LENGTH):
        self.grid = Grid(grid, row_length)
        self.grid_lookup = GridLookup(self.grid, index_length)

    def is_present(self, word):
        word = word.strip().lower()
        if len(word) <= self.grid_lookup.max_word_length:
            return self.grid_lookup.is_present(word)
        else:
            for grid_index in self.grid_lookup.get_grid_indexes(word):
                if self.grid.is_present_in_row(grid_index, word) or \
                        self.grid.is_present_in_column(grid_index, word):
                    return True


if __name__ == '__main__':

    with open('grid') as rp:
        grid = rp.read()

    with open('/usr/share/dict/words') as rp:
        words_to_find = rp.readlines()

    ws = WordSearch(grid)

    for word in words_to_find:
        if ws.is_present(word):
            print 'Found: {}'.format(word)
