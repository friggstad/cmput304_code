import random

# change this if wanted
minval = 1
maxval = 8
n = 22

d = [[random.randint(minval, maxval) if i != j else 0 for j in range(n)] for i in range(n)]
print(n)
for row in d: print(*row)
