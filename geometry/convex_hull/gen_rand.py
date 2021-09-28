import random

# returns true iff at least two points are the same or the three are collinear
def collinear(p, q, r):
    x1, y1 = p[0]-q[0], p[1]-q[1]
    x2, y2 = r[0]-q[0], r[1]-q[1]
    return x1*y2 == x2*y1

if __name__ == "__main__":
    pts = []
    mdim = 1000000000
    while len(pts) < 300:
        p = (random.randint(-mdim, mdim), random.randint(-mdim, mdim))
        if p in pts: continue
        bad = False
        for i in range(len(pts)):
            for j in range(i):
                if collinear(pts[i], pts[j], p):
                    bad = True
        if bad: continue
        pts.append(p)

    print(len(pts))
    for p in pts: print(*p)
