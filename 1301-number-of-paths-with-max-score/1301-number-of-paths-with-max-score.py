class Solution:
    def pathsWithMaxScore(self, board):
        MOD = 10**9 + 7
        n = len(board)

        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        ways = [[0] * (n + 1) for _ in range(n + 1)]

        dp[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1

        directions = [(1, 0), (0, 1), (1, 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] == 'X' or board[i][j] == 'S':
                    continue

                best = -1
                count = 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if ni < n and nj < n:
                        if dp[ni][nj] > best:
                            best = dp[ni][nj]
                            count = ways[ni][nj]
                        elif dp[ni][nj] == best and best != -1:
                            count = (count + ways[ni][nj]) % MOD

                if best == -1:
                    continue

                dp[i][j] = best
                ways[i][j] = count

                if board[i][j].isdigit():
                    dp[i][j] += int(board[i][j])

        if ways[0][0] == 0:
            return [0, 0]

        return [dp[0][0], ways[0][0]]