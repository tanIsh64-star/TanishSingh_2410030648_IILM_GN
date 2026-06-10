import heapq

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        lg = [0] * (n + 1)
        for i in range(2, n + 1):
            lg[i] = lg[i // 2] + 1

        m = lg[n] + 1

        mx = [[0] * m for _ in range(n)]
        mn = [[0] * m for _ in range(n)]

        for i in range(n):
            mx[i][0] = nums[i]
            mn[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            half = 1 << (j - 1)
            for i in range(n - (1 << j) + 1):
                mx[i][j] = max(mx[i][j - 1], mx[i + half][j - 1])
                mn[i][j] = min(mn[i][j - 1], mn[i + half][j - 1])
            j += 1

        def value(l, r):
            p = lg[r - l + 1]
            mxv = max(mx[l][p], mx[r - (1 << p) + 1][p])
            mnv = min(mn[l][p], mn[r - (1 << p) + 1][p])
            return mxv - mnv

        heap = []

        for l in range(n):
            v = value(l, n - 1)
            heapq.heappush(heap, (-v, l, n - 1))

        ans = 0

        for _ in range(k):
            v, l, r = heapq.heappop(heap)
            ans -= v

            if r > l:
                nv = value(l, r - 1)
                heapq.heappush(heap, (-nv, l, r - 1))

        return ans