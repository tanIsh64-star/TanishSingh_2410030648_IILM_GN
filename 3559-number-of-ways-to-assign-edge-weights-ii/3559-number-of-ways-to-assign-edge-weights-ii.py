class Solution:
    def assignEdgeWeights(self, edges, queries):
        MOD = 1000000007
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = 17
        while (1 << LOG) <= n:
            LOG += 1

        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        stack = [(1, 0)]
        while stack:
            u, p = stack.pop()
            parent[0][u] = p
            for v in g[u]:
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u))

        for j in range(1, LOG):
            for i in range(1, n + 1):
                parent[j][i] = parent[j - 1][parent[j - 1][i]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]
            for j in range(LOG):
                if diff & (1 << j):
                    a = parent[j][a]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if parent[j][a] != parent[j][b]:
                    a = parent[j][a]
                    b = parent[j][b]

            return parent[0][a]

        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            w = lca(u, v)
            k = depth[u] + depth[v] - 2 * depth[w]

            if k == 0:
                ans.append(0)
            else:
                ans.append(pow2[k - 1])

        return ans