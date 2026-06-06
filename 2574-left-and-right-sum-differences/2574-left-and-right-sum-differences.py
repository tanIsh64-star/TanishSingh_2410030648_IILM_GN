class Solution:
    def leftRightDifference(self, nums):
        left = 0
        right = sum(nums)
        ans = []

        for num in nums:
            right -= num
            ans.append(abs(left - right))
            left += num

        return ans