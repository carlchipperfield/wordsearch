import random
import string

s = ''.join(random.choice(string.ascii_lowercase) for _ in xrange(10000 ** 2))

with open('grid', 'w') as rp:
    rp.write(s)
