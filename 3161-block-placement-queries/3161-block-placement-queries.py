from bisect import bisect_left
from sortedcontainers import SortedList


class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * (4 * n)

    def update(self, idx, val, node, l, r):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)

        self.seg[node] = max(
            self.seg[node * 2],
            self.seg[node * 2 + 1]
        )

    def query(self, ql, qr, node, l, r):
        if qr < l or r < ql:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(ql, qr, node * 2, l, mid),
            self.query(ql, qr, node * 2 + 1, mid + 1, r)
        )


class Solution:
    def getResults(self, queries):
        MX = min(50000, len(queries) * 3) + 5

        seg = SegmentTree(MX + 1)

        obstacles = SortedList([0, MX])

        seg.update(MX, MX, 1, 0, MX)

        ans = []

        for q in queries:
            if q[0] == 1:
                x = q[1]

                i = obstacles.bisect_left(x)

                prev = obstacles[i - 1]
                nxt = obstacles[i]

                seg.update(x, x - prev, 1, 0, MX)
                seg.update(nxt, nxt - x, 1, 0, MX)

                obstacles.add(x)

            else:
                _, x, sz = q

                i = obstacles.bisect_right(x) - 1
                prev = obstacles[i]

                tail = x - prev
                best = seg.query(0, x, 1, 0, MX)

                ans.append(max(best, tail) >= sz)

        return ans