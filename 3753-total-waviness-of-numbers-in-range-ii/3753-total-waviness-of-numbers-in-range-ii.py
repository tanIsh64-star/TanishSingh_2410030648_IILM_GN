class Solution:
    def totalWaviness(self, num1, num2):

        def solve(x):
            if x < 0:
                return 0

            s = str(x)
            memo = {}

            def dp(pos, prev1, prev2, started, tight):
                key = (pos, prev1, prev2, started, tight)

                if key in memo:
                    return memo[key]

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, -1, -1, False, ntight)
                    else:
                        add = 0

                        if started and prev2 != -1:
                            if ((prev1 > prev2 and prev1 > d) or
                                (prev1 < prev2 and prev1 < d)):
                                add = 1

                        cnt, wav = dp(
                            pos + 1,
                            d,
                            prev1 if started else -1,
                            True,
                            ntight
                        )

                        wav += add * cnt

                    total_cnt += cnt
                    total_wav += wav

                memo[key] = (total_cnt, total_wav)
                return memo[key]

            return dp(0, -1, -1, False, True)[1]

        return solve(num2) - solve(num1 - 1)