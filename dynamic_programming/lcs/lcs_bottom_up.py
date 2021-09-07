# Bottom-up implementation of the longest common subsequence algorithm.
# See lcs_sample1.txt for an example of how to format the input.
#
# This code also recovers a sequence.


# Returns an LCS of the two sequences.
# memo can be an empty dictionary or one that has some lcs(i,j) values
# already computed.
def lcs(seq1, seq2):
    # feel free to switch to a 2D list if you don't like the fact that
    # hash tables don't guarantee O(1) access time
    n, m = len(seq1), len(seq2)
    memo = {}

    # compute the table entries
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                memo[(i, j)] = 0
            elif seq1[i-1] == seq2[j-1]:
                memo[(i, j)] = 1 + memo[(i-1, j-1)]
            else:
                memo[(i, j)] = max(memo[(i-1, j)], memo[(i, j-1)])

    answer = []
    i, j = n, m

    # now backstep along the table to recover the actual sequence
    while i > 0 and j > 0:
        if seq1[i-1] == seq2[j-1]:
            answer.append(seq1[i-1]) # this will build the answer in reverse order
            i -= 1
            j -= 1
        elif memo[(i-1, j)] >= memo[(i, j-1)]:
            i -= 1
        else:
            j -= 1
    return answer[::-1]

if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))

    ans = lcs(seq1, seq2)
    print("LCS length:", len(ans))

    # now let's actually recover a longest common subsequence
    print(*ans)
