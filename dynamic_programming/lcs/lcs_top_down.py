import functools # see decorator below, it automatically memoizes the function
import sys

# have to let sequences be global variables so they don't get
# inserted into the memo table each time
@functools.lru_cache(maxsize=None)
def lcs(i, j):
    if i == 0 or j == 0:
        return 0
    elif seq1[i-1] == seq2[j-1]:
        return 1 + lcs(i-1, j-1)
    else:
        return max(lcs(i-1, j), lcs(i, j-1))

if __name__ == "__main__":
    n, m = map(int, input().split())
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))

    # python's default recursion limit is 1000, not enough for the big example
    sys.setrecursionlimit(n*m+10)

    print("LCS length:", lcs(n, m))
