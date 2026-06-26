class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 2)

    def update(self, idx, val):
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def query(self, idx):
        s = 0
        while idx > 0:
            s += self.bit[idx]
            idx -= idx & -idx
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        bit = BinaryIndexedTree(2 * n + 2)

        prefix = n + 1
        bit.update(prefix, 1)

        ans = 0

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            ans += bit.query(prefix - 1)
            bit.update(prefix, 1)

        return ans