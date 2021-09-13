# generates m random d-dimensional vectors plus a weight for each

import random

m = 50
d = 30

print(m)

for i in range(m): print(*[random.randint(-1000, 1000) for i in range(d)]+[random.randint(1, 1000000)])
