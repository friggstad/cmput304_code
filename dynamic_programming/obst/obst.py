# Optimal BST dynamic programming algorithm.
# Running time: O(n^3)
# sample.txt is the sample from Figure 15.9

import sys
import functools

# return q[i-1] + p[i] + q[i] + p[i+1] + ... + q[j-1] + p[j] + q[j]
# just returns q[i-1] if j == i-1
@functools.lru_cache(maxsize=None)
def tot(i, j):
    if j == i-1: return q[j]
    return q[i-1] + p[i] + tot(i+1, j)

@functools.lru_cache(maxsize=None)
def obst(i, j):
    if j == i-1: return 0.0
    return min(obst(i, k-1) + obst(k+1, j) + tot(i, j) - p[k] for k in range(i, j+1))

if __name__ == "__main__":
    n = int(input())

    # recursion depth is <= n since each recursive call is
    # to a strictly smaller interval, but Python has a few function calls
    # on the stack (eg. the min() function) as well. 5*n turns out to be ok.
    sys.setrecursionlimit(5*n)

    # the extra 0.0 is a dummy entry so we can 1-index
    # it just like the pseudocode
    p = [0.0] + list(map(float, input().split()))
    q = list(map(float, input().split()))

    print("Optimal BST Cost: {0:.08f}".format(obst(1, n)))
