# Word search

### Problem

Consume a word search grid and enable fast searching of words

### Design

On initialisation, the grid of letters is processed to generate a lookup table
implemented as a tree of dictionaries. Each letter of the grid is stored in
the root dictionary with the next INDEX_LENGTH letters along the same row/column
stored as child nodes. If there are more letters remaining in the row or column then
the index of the letter is added to a list in the leaf dictionary.

An example of the lookup table, with INDEX_LENGTH set to 3:

```
A -> N -> E -> [2]
  -> A -> I -> [1, 4, 5]
  -> C
B -> E
H -> E -> L -> [2, 4]
```

When searching for a word whose length is less than or equal to INDEX_LENGTH
the lookup table is traversed to find a match. For longer words the first
INDEX_LENGTH letters of the word are searched in the lookup table to find a list
of potential indexes in the grid. The grid is then searched at each index,
trying to match the word along the same row and column.

### Bonus question

The initial indexing of the grid is time consuming and should be split
into different units of work. A pool of worker processes could be used
with each process responsible for indexing x letters of the grid. The
output of each process would be a GridLookup object which can then be
exchanged with the main process using message passing. Each GridLookup object
would then be merged into a single GridLookup object representing the
whole grid.

The word search implementation could be refactored using the multiprocessing
module. The multiprocessing module provides message passing implementations,
such as Queue, which could be used to exchange the GridLookup objects.

Python threads should not be used for this solution as they are not executed in
parallel, they only provide interleaving. As the word search problem is CPU
intensive threads would provide no benefits.