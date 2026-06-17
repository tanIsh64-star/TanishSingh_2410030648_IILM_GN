class Solution:
    def processStr(self, s, k):
        n = len(s)

        length = [0] * (n + 1)

        for i in range(n):
            ch = s[i]
            cur = length[i]

            if 'a' <= ch <= 'z':
                length[i + 1] = cur + 1
            elif ch == '*':
                length[i + 1] = max(0, cur - 1)
            elif ch == '#':
                length[i + 1] = cur * 2
            else:  # '%'
                length[i + 1] = cur

        if k >= length[n]:
            return '.'

        for i in range(n - 1, -1, -1):
            ch = s[i]

            if 'a' <= ch <= 'z':
                if k == length[i]:
                    return ch

            elif ch == '*':
                if k >= length[i]:
                    k = length[i] - 1

            elif ch == '#':
                if k >= length[i]:
                    k -= length[i]

            else:  # '%'
                if length[i] > 0:
                    k = length[i] - 1 - k

        return '.'