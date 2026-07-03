from heapq import heappush, heappop

class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        n = len(online)
        g = [[] for _ in range(n)]

        INF = 10 ** 18
        left = INF
        right = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue
            g[u].append((v, w))
            if w < left:
                left = w
            if w > right:
                right = w

        if left == INF:
            return -1

        def check(mid):
            dist = [INF] * n
            dist[0] = 0
            pq = [(0, 0)]

            while pq:
                d, u = heappop(pq)
                if d != dist[u]:
                    continue
                if d > k:
                    continue
                if u == n - 1:
                    return True

                for v, w in g[u]:
                    if w < mid:
                        continue
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))

            return False

        ans = -1
        l = left
        r = right

        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans