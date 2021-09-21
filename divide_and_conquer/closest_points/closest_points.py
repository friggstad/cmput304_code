# Closest pair of points in O(n log^2 n) time
# points are represented as a tuple of coordinates: (x, y)
#
# The textbook discusses how to get it down to O(n log n) time but it takes
# extra work coding. I won't bother unless someone really wants to see it,
# but I am happy doing it if someone is actually interested (send me an email)

import math

def dist2(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2)

# simple O(n^2) version of closest pair
# assumes there are at least 2 points
def brute_force(pts):
    delta = dist2(pts[0], pts[1]) + 1
    for i in range(len(pts)):
        for j in range(i):
            tmp = dist2(pts[i], pts[j])
            if tmp < delta:
                delta = tmp
                p, q = pts[i], pts[j]
    return p, q

# returns the closest pair of points
# assumes there are at least 2 points
def closest_pair(pts, init = True):
    # sort the points by x coordinate if this is the first recursive call
    if init: pts.sort()

    if len(pts) <= 3:
        return brute_force(pts)

    # if we get here, len(pts) >= 4
    n = len(pts)
    p1, q1 = closest_pair(pts[:n//2], False)
    p2, q2 = closest_pair(pts[n//2:], False)

    # note which of the two pairs was closest
    d1 = dist2(p1, q1)
    d2 = dist2(p2, q2)
    if d1 < d2:
        p, q = p1, q1
        delta = d1
    else:
        p, q = p2, q2
        delta = d2

    mid_x = pts[n//2][0]

    # get the points that are within distance delta of the vertical line
    # passing through mid_x
    strip = [p for p in pts if abs(p[0] - mid_x) <= delta]

    # sort them by y value
    strip.sort(key = lambda p : p[1])

    # for each point in the strip, look at the next 20 points
    # to see if we find a closer pair
    for i in range(len(strip)):
        for j in range(i+1, min(len(strip), i+20)):
            tmp = dist2(strip[i], strip[j])
            if tmp < delta:
                delta = tmp
                p, q = strip[i], strip[j]
    return p, q

if __name__ == "__main__":
    n = int(input())
    pts = [tuple(map(int, input().split())) for i in range(n)]

    p, q = closest_pair(pts)
    print("Closest pair:", p, q)
    print("Distance: {0:.08f}".format(dist2(p,q)))

    # brute force check to verify the answer is correct
    # runs much slower than the algorithm we just ran
    print("Running brute force check (might be very slow on large inputs)")
    p2, q2 = brute_force(pts)
    assert abs(dist2(p, q) - dist2(p2, q2)) < 1e-9
    print("Check passed")
