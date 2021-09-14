# Maximum-weight matching in a tree in O(n) time.
# Input assumes nodes are numbered 0 through n-1, 0 is the root,
# and node i has parent < i
#
# So the input consists of n
# and then n-1 pairs (p, w) where for the i'th pair (1 <= i <= n-1)
# we have p is the parent of node i and the edge has weight w

import sys

# - (v,b) is the subproblem (v a node, b = 1 or 0 indicating if v is free
# to match with a child)
# - tree[v] is the pair (u,w) where u is a child of v and w
# is the weight of this edge
# - memo[(v,b)] stores the pair (val, dec)
# where dec = None if we don't match v to a child in the optimum, otherwise
# dec is the child that we match v to
# Returns the optimum value of this subproblem.
def matching(v, b, tree, memo):
    if (v, b) not in memo:
        if not tree[v]:
            # if v is a leaf
            memo[(v, b)] = (0, None)
        else:
            # compute total value of subproblems (u,0) for children u of v
            tot_0 = sum(matching(u, 0, tree, memo) for u, w in tree[v])
            memo[(v, b)] = (tot_0, None)

            # if we are allowed to match v to a child, try it
            if b == 0:
                for u, w in tree[v]:
                    tmp = tot_0 - matching(u, 0, tree, memo) + matching(u, 1, tree, memo) + w
                    if tmp > memo[(v, b)][0]: memo[(v, b)] = (tmp, u)

    return memo[(v, b)][0]

def print_matching(v, b, tree, memo):
    # if not a leaf node
    if tree[v]:
        for u, w in tree[v]:
            if u == memo[(v, b)][1]:
                # if this (v,b) subproblem matched v to u, print the edge
                print(v, u, w)
                print_matching(u, 1, tree, memo)
            else:
                print_matching(u, 0, tree, memo)

if __name__ == "__main__":
    n = int(input())
    tree = {i:[] for i in range(n)}
    for i in range(n-1):
        p, w = map(int, input().split())
        tree[p].append((i+1, w))

    sys.setrecursionlimit(5*n)

    memo = {}
    matching(0, 0, tree, memo)
    print("Edges in the matching (u, v, weight):")
    print_matching(0, 0, tree, memo)
    print("Optimal matching cost:", memo[(0, 0)][0])
