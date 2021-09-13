# implementation of Huffman tree algorithm and a few sample compressions

import heapq # import a min heap

# a tree node will be (freq, letter, left_child, right_child)
# using NONE when not applicable

# recursively prints the binary encoding of all input characters
def encode_print(trees, bits, encode):
    if trees[1] is None:
        encode_print(trees[2], bits+"0", encode)
        encode_print(trees[3], bits+"1", encode)
    else:
        print("{0}: {1}".format(trees[1], bits))
        encode[trees[1]] = bits

if __name__ == "__main__":
    n = int(input())
    assert n >= 2 # need at least 2 symbols for this to make sense

    comp = lambda x : x[2]

    # get all singleton trees corresponding to input values
    trees = []
    for i in range(n):
        letter, freq = input().split()
        heapq.heappush(trees, (int(freq), letter, None, None))

    # run the greedy algorithm
    while len(trees) > 1:
        x = heapq.heappop(trees)
        y = heapq.heappop(trees)
        heapq.heappush(trees, (x[0]+y[0], None, x, y))

    encode = {}
    print("Encoding table is")
    encode_print(trees[0], "", encode)

    for _ in range(int(input())):
        msg = input()
        enc_msg = [encode[c] for c in msg]
        print()
        print(msg, "encoding is")
        print(*enc_msg, sep="")
