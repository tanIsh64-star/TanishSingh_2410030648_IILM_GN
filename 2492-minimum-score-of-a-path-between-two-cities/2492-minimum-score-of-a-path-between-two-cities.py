from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = [False] * (n + 1)
        ans = [float('inf')]

        def dfs(node):
            visited[node] = True
            for nei, w in graph[node]:
                if w < ans[0]:
                    ans[0] = w
                if not visited[nei]:
                    dfs(nei)

        dfs(1)
        return ans[0]