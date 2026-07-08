class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 1000000007
        n = len(s)

        cnt = [0] * (n + 1)
        sm = [0] * (n + 1)
        pref = [0] * (n + 1)
        pw = [1] * (n + 1)

        for i in range(n):
            pw[i + 1] = (pw[i] * 10) % MOD

        for i in range(n):
            d = ord(s[i]) - ord('0')
            cnt[i + 1] = cnt[i]
            sm[i + 1] = sm[i]
            pref[i + 1] = pref[i]

            if d != 0:
                cnt[i + 1] += 1
                sm[i + 1] += d
                pref[i + 1] = (pref[i] * 10 + d) % MOD

        ans = []

        for l, r in queries:
            c1 = cnt[l]
            c2 = cnt[r + 1]
            k = c2 - c1

            x = (pref[r + 1] - pref[l] * pw[k]) % MOD
            digit_sum = sm[r + 1] - sm[l]

            ans.append((x * digit_sum) % MOD)

        return ans