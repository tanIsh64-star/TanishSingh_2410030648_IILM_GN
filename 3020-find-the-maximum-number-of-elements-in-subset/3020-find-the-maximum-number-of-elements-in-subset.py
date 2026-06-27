from collections import Counter

class Solution:
    def maximumLength(self, nums):
        cnt = Counter(nums)

        ans = 1

        if 1 in cnt:
            ans = cnt[1]
            if ans % 2 == 0:
                ans -= 1

        for start in cnt:
            if start == 1:
                continue

            x = start
            length = 0

            while cnt[x] >= 2:
                length += 2
                x *= x

            if x in cnt:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans