class Solution:
    def maxBuilding(self, n, restrictions):
        restrictions.append([1, 0])
        restrictions.sort()

        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])

        m = len(restrictions)

        # Left to Right
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] +
                restrictions[i][0] - restrictions[i - 1][0]
            )

        # Right to Left
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] +
                restrictions[i + 1][0] - restrictions[i][0]
            )

        ans = 0

        for i in range(m - 1):
            x1, h1 = restrictions[i]
            x2, h2 = restrictions[i + 1]

            ans = max(
                ans,
                (h1 + h2 + x2 - x1) // 2
            )

        return ans