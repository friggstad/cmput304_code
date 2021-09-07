# generates a random LCS instance

import random

# comment this out if you want a different random sequence each time
random.seed(0)

n = 1000
m = 1100

# generate a length-l random sequence of values from 0 to 100
# try changing the 100 to a different value to see how the LCS size
# typically changes
def genrand(l):
    return [random.randint(0, 100) for _ in range(l)]

print(n, m)
print(*genrand(n))
print(*genrand(m))
