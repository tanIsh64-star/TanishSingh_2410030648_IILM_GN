class Solution(object):
    def numberOfSubstrings(self, s):
        last = [-1, -1, -1]
        ans = 0

        for i in range(len(s)):
            last[ord(s[i]) - ord('a')] = i
            ans += min(last) + 1

        return ans