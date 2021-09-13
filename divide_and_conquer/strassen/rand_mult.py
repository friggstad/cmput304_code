import random

def rand_matrix(n):
    return [[random.randint(-1000, 1000) for j in range(n)] for i in range(n)]

n = 128

# ensure a power of 2
assert n >= 1 and (n&(n-1)) == 0

print(n)
for r in rand_matrix(n): print(*r)
for r in rand_matrix(n): print(*r)
