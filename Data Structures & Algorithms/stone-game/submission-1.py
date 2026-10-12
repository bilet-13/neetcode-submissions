from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        # @cache
        # def play(i, j):
        #     if i > j:
        #         return (0, 0)

        #     a1, b1 = play(i + 1, j)
        #     a2, b2 = play(i, j - 1)

        #     taken = n - (j - i + 1)
        #     if taken % 2 == 0:
        #         left = (a1 + piles[i], b1)
        #         right = (a2 + piles[j], b2)
        #         return max(left, right, key=lambda x: x[0])
        #     else:
        #         left = (a1, b1 + piles[i])
        #         right = (a2, b2 + piles[j])
        #         return max(left, right, key=lambda x:x[1])
        
        # alice, bob = play(0, len(piles) - 1)
        # return alice > bob

        dp = [[(0, 0) for _ in range(n)] for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                a1, b1 = dp[i + 1][j] if i + 1 <= j else (0, 0)
                a2, b2 = dp[i][j - 1] if i <= j - 1 else (0, 0)

                taken = n - (j - i + 1)
                if taken % 2 == 0:
                    left = (a1 + piles[i], b1)
                    right = (a2 + piles[j], b2)
                    dp[i][j] = left if left[0] > right[0] else right

                else:
                    left = (a1, b1 + piles[i])
                    right = (a2, b2 + piles[j])
                    dp[i][j] = left if left[1] > right[1] else right
        
        return dp[0][n - 1][0] > dp[0][n - 1][1] 



