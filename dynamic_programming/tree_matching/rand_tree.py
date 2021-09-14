# this tends to make really short trees

import random

n = 100000

print(n)
for i in range(n-1):
    print(random.randint(0,i), random.randint(1, 1000))
    # above makes a short tree
    # to make a deep tree, use the following instead
    # print(random.randint(max(0, i-20),i), random.randint(1, 1000))
