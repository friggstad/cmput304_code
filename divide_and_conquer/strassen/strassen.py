# Strassen's method for matrix multipliciation
# O(n^{log_2(7)}), note log_2(7) is a bit less than 2.8074
# Will not outpeform classic O(n^3) in practice since n needs to be
# INCREDIBLY large with this implementation (no optimizations were performed,
# such as indexing in place rather than copying matrices).
#
# Throughout: assumes n is a power of 2

# splits a square matrix M (even dimension) into 4 equal-size parts
def split_matrix(M):
    n2 = len(M)//2
    M11 = [M[i][:n2] for i in range(n2)]
    M12 = [M[i][n2:] for i in range(n2)]
    M21 = [M[i+n2][:n2] for i in range(n2)]
    M22 = [M[i+n2][n2:] for i in range(n2)]
    return M11, M12, M21, M22

# merges the 4 arguments representing the 4 "parts" of a matrix
# into a single matrix. assumes they are all square of the same dimension
def merge_matrix(M11, M12, M21, M22):
    n = len(M11)
    return [M11[i]+M12[i] for i in range(n)] + [M21[i]+M22[i] for i in range(n)]

# adds two square matrices of the same dimension
def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

# subtracts two square matrices of the same dimension
def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

# assums A, B are both square matrices of the same dimension n
# and that n is a power of 2
def strassen(A, B):
    n = len(A)

    # base case, just do it
    if n == 1:
        return [[A[0][0]*B[0][0]]]

    # using same notation from the textbook (Chapter 4.2)
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    S1 = sub(B12, B22)
    S2 = add(A11, A12)
    S3 = add(A21, A22)
    S4 = sub(B21, B11)
    S5 = add(A11, A22)
    S6 = add(B11, B22)
    S7 = sub(A12, A22)
    S8 = add(B21, B22)
    S9 = sub(A11, A21)
    S10 = add(B11, B12)

    P1 = strassen(A11, S1)
    P2 = strassen(S2, B22)
    P3 = strassen(S3, B11)
    P4 = strassen(A22, S4)
    P5 = strassen(S5, S6)
    P6 = strassen(S7, S8)
    P7 = strassen(S9, S10)

    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)

    C = merge_matrix(C11, C12, C21, C22)

    return C

# classic matrix multiplication
# assumes both matrices are square of the same dimension
# O(n^3)
def classic_multiply(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


if __name__ == "__main__":
    n = int(input())

    # check n is a power of 2
    assert n >= 1 and n&(n-1) == 0

    A = [list(map(int, input().split())) for i in range(n)]
    B = [list(map(int, input().split())) for i in range(n)]

    C = strassen(A, B)

    print(C)

    # double check against simple O(n^3) for correctness
    # note: classic_multiply will be faster in practice
    # since I haven't spent any time optimizing the implementation
    assert C == classic_multiply(A, B)
