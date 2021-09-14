import random

def rand_point():
    return tuple(random.randint(-1000000, 1000000) for i in range(2))

n = 20000

print(n)
for i in range(n): print(*rand_point())
