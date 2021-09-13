# uses the Fraction class so we can do row reductions without worrying
# about floating point issues when checking if something is 0
# assumes the input vectors have integer values
#
# Running time: O(m log m + m*d^3) where d is the dimension
# (this does not take advantage of the speedup mentioned in the slides,
# but that wouldn't be too hard to do givein this code)

from fractions import Fraction
import copy

# Returns the reduced row echelon form of M
# Assumption: M is a 2-dimensional list of fractions
#    representing a rectangular matrix
# Running time O(rows * cols^2)
# Would be O(rows * cols) if, apart from the last row, it was already RREF
# (helpful if you want to consider trying the speedup)
def rref(old_M):
    M = copy.deepcopy(old_M)

    nr, nc = len(M), len(M[0])

    # invariant: rows < r are in RREF
    # and M[i][j] = 0 for all i >= r, j < c
    r = 0
    for c in range(nc):
        # find a "pivot" row, a row >= r with a nonzero entry in column c
        piv = r
        while piv < nr and M[piv][c] == 0:
            piv += 1

        # if this is true, column c was already 0 at indices >= r
        if piv == nr: continue

        # otherwise, swap this pivot row to row r
        M[r], M[piv] = M[piv], M[r]

        # normalize the row so it has a leading 1
        for j in range(nc-1, c-1, -1): M[r][j] /= M[r][c]
        # now add a multiple of row r to all other rows to
        # get 0s in every other entry in this column
        for i in range(0, nr):
            if i != r and M[i][c] != 0:
                for j in range(nc-1, c-1, -1): M[i][j] -= M[r][j] * M[i][c]
        r += 1
    return M

# is the given list of row vectors independent?
# can view "vecs" as a matrix whose rows are the vectors in question
def is_independent(vecs):
    # If you recall standard linalg, if you use row operations on a matrix,
    # the last row is nonzero if and only if the rows were independent
    #
    # So, we return True if and only if in the RREF form of the matrix
    # of given vectors, there is a nonzero entry in the last row.

    return any(rref(vecs)[-1])



if __name__ == "__main__":
    # num vectors, the dimension will be inferred from the input
    # assumes all input vectors have the same length
    # the last entry for each vector will be its weight, see sample.txt
    # for the example corresponding to the slides
    m = int(input())
    inp_vecs = []
    for i in range(m):
        # read the vector/weights and split it up properly
        a = list(map(Fraction, input().split()))

        # only add it if the weight is nonnegative
        if a[-1] >= 0: inp_vecs.append((a[:-1], a[-1]))

    # sort by weight and then reverse
    inp_vecs.sort(key = lambda x : x[-1])
    inp_vecs = inp_vecs[::-1]

    solution = []
    for vec, w in inp_vecs:
        # try adding this vector to our solution and see if it maintains independence
        if is_independent([x[0] for x in solution] + [vec]):
            solution.append((vec, w))

    print("Weight of vectors chosen:", sum(a[-1] for a in solution))
    print("Number of vectors chosen:", len(solution))
    for vec, w in solution:
        print(*map(int, vec), "   having weight", w)
