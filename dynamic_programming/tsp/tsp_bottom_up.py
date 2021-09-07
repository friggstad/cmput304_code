# bottom-up DP implementation
# Python is terrible with 2D lists, this will run WAY slower than
# the same C++ implementation in practice

# does the integer representing set S contain vertex v?
def contains(S, v):
    return True if ((S>>v)&1) == 1 else False

# remove v from S, assumes it was there already
def remove(S, v):
    return S^(1<<v)

def setsize(S):
    # add the 1 bits
    return sum((S>>i)&1 for i in range(n))

if __name__ == "__main__":
    n = int(input())

    # read the matrix
    d = [list(map(int, input().split())) for i in range(n)]

    memo = [[0]*n for i in range(2**n)] # store the cost
    backtrace = [[0]*n for i in range(2**n)] # store the previous node in the best solution

    # bigger than any path cost, (n+1) * maximum input value
    INF = (n+1)*max(max(row) for row in d)

    for S in range(2**n):
        # check the root is in S and S is not just representing {0}
        if contains(S, 0) and S != 1:
            for v in range(1,n):
                if contains(S, v):
                    # start processing subproblem (S,v)
                    if setsize(S) == 2:
                        memo[S][v] = d[0][v]
                        backtrace[S][v] = 0
                    else:
                        memo[S][v] = INF
                        for u in range(1,n):
                            if u != v and contains(S, u):
                                pS = remove(S, v)
                                val = memo[pS][u] + d[u][v]
                                if val < memo[S][v]:
                                    memo[S][v] = val
                                    backtrace[S][v] = u

    S = 2**n-1
    v = 1
    for u in range(2, n):
        if memo[S][u] + d[u][0] < memo[S][v] + d[v][0]:
            v = u
    print("TSP Cost:", memo[S][v] + d[v][0])
    tour = [v]
    while S != 1:
        u = backtrace[S][v]
        tour.append(u)
        S = remove(S, v)
        v = u
    tour = tour[::-1]
    print(*tour)
