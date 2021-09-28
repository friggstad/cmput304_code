import random

n = 200

x_vals = set()
while len(x_vals) < n: x_vals.add(random.randint(1, 10000))

print(n)
for x in x_vals:
    print(x, random.randint(1, 10000))
