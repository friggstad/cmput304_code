import random

n = 1000
l = 1000

prefix = "a"*(l-10)

print(n)

for _ in range(n):
    s = prefix
    while len(s) < l:
        s += random.choice("ab")
    print(s)
