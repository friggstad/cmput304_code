# an implementation of the algorithm from 16.5 of the book
# running time: O(n^2 * log n)
# See exercise 16-4 for a faster way to implement it: O(n log n).

# throughout: a job will be a pair (d_i, w_i): deadline & weight

# is the list of jobs feasible?
def feasible(jobs):
    ordered = sorted(jobs)
    for i in range(len(ordered)):
        if ordered[i][0] <= i: # remember, i will be a 0-based index
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    in_jobs = list(tuple(map(int, input().split())) for i in range(n))

    # sort in reverse order of weight
    in_jobs.sort(key = lambda x : -x[1])

    jobs = []
    value = 0
    penalty = 0
    for d, w in in_jobs:
        if feasible(jobs+[(d,w)]):
            value += w
            jobs.append((d,w))
        else:
            penalty += w

    print("Total value of scheduled jobs:", value)
    print("Penalty of missed jobs:", penalty)
    print("Number of scheduled jobs:", len(jobs))

    # print the scheduled jobs in the order they should be completed
    print("Jobs completed (in order of their processing time)")
    for d, w in sorted(jobs): print(d, w)
