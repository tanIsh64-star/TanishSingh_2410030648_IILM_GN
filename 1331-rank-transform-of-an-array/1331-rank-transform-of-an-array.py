class Solution:
    def arrayRankTransform(self, arr):
        rank = {}

        for i, num in enumerate(sorted(set(arr))):
            rank[num] = i + 1

        return [rank[num] for num in arr]