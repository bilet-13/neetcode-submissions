class Solution:
    def integerBreak(self, n: int) -> int:
        # dp
        # dp[i] = the maximize product of the positive integers
        # dp[2] = 1
        # dp[3] = 1 * dp[2]
        # dp[4] = max(1 * dp[3], 2 * dp[2],)
        #      # dp[5] = max(1 * dp[4], 2 * dp[3], 3* dp[2], 4 * dp[1])

        dp = [1 for _ in range(n + 1)]

        for i in range(3, n + 1):
            for j in range(1, i - 1):
                dp[i] = max(dp[i], j * dp[i - j], j * (i - j))


        return dp[n]


        