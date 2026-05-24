class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            ans = 1

            # Move right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            # Move left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            dp[i] = ans
            return ans

        result = 1

        for i in range(n):
            result = max(result, dfs(i))

        return result