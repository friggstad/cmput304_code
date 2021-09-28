# bitonic TSP implementation
# assumes (for simplicity) no two x-values have the same coordinate

import functools, math


def dist2(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

# treats pts as a global array so it doesn't get cached automatically
# assumes i < j
@functools.lru_cache(maxsize=None)
def bitonic_tsp(i, j):
    # in this case case,
    # the point prior to j must have been visited by the path ending at j
    if i+1 < j: return bitonic_tsp(i, j-1) + dist2(pts[j], pts[j-1])

    # now 0 <= i and j == i+1

    # base case
    if i == 0: return dist2(pts[0], pts[1])

    # final case, 0 < i and j == i+1, we guess the node prior to j on that path
    return min(bitonic_tsp(k, i) + dist2(pts[k], pts[j]) for k in range(i))


if __name__ == "__main__":
    n = int(input())
    pts = [tuple(map(int, input().split())) for i in range(n)]
    pts.sort() # sort by x value

    answer = min(bitonic_tsp(k, n-2) + dist2(pts[k], pts[n-1]) + dist2(pts[n-2], pts[n-1]) for k in range(n-2))
    print("Optimum bitonic TSP tour cost: {0:.08f}".format(answer))
