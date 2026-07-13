class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []

        for start in range(1, 9):
            num = start
            for nxt in range(start + 1, 10):
                num = num * 10 + nxt
                if low <= num <= high:
                    ans.append(num)

        ans.sort()
        return ans