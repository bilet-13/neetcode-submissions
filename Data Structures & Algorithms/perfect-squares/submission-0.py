class Solution:
    def numSquares(self, n: int) -> int:
        # dp
        # dp[i] = the least number of perfect square numbers that sum to n
        #need to calculate perfect square
        perfect_squares = []

        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0

        for i in range(1, math.floor(n ** 0.5) + 1):
            perfect_squares.append(i * i)
            dp[i * i] = 1


        for i in range(1, n + 1):
            for num in perfect_squares:
                if i - num < 0:
                    break

                dp[i] = min(dp[i], dp[num] + dp[i - num])

        return dp[n]
                

        