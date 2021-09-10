# generates 2*N+1 random probabilities by sampling each to be a value
# between 0 and 1000000 and then normalizing so they sum to 1
#
# doesn't do a good job creating an interesting example where some items
# have large probability and others have small probability

import random

N = 100

values = [random.randint(0, 1000000) for i in range(2*N+1)]
tot = sum(values)
values = list(map(lambda x : x/tot, values))
print(N)
print(*values[1::2])
print(*values[::2])
