import random

n = 100000
m = 1000000
maxw = 1000000000

assert m <= n*(n-1)//2

# returns a random pair u,v with 1 <= u < v <= n
# we ensure u < v so that a single edge is not represented twice
# in the edges set
def randedge():
    u = v = 1
    while u == v:
        u, v = random.randint(1, n), random.randint(1, n)
    return (min(u,v), max(u,v))

print(n, m)
edges = set()
# be careful, if m is too big (close to (n choose 2)) this may take too long
while len(edges) < m:
    edges.add(randedge())

for u, v in edges:
    print(u, v, random.randint(1, maxw))
