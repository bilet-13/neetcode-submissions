from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @cache
        def play(i, j):
            if i > j:
                return (0, 0)

            opp1, me1 = play(i + 1, j)
            opp2, me2 = play(i, j - 1)

            
            left = (me1 + piles[i], opp1)
            right = (me2 + piles[j], opp2)

            return left if left[0] > right[0] else right
            
        
        alice, bob = play(0, len(piles) - 1)
        return alice > bob

        # dp = [[(0, 0) for _ in range(n + 1)] for _ in range(n + 1)]
        
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n + 1):
        #         a1, b1 = dp[i + 1][j] 
        #         a2, b2 = dp[i][j - 1] 

        #         taken = n - (j - i)
        #         if taken % 2 == 0:
        #             left = (a1 + piles[i], b1)
        #             right = (a2 + piles[j - 1], b2)
        #             dp[i][j] = left if left[0] > right[0] else right

        #         else:
        #             left = (a1, b1 + piles[i])
        #             right = (a2, b2 + piles[j - 1])
        #             dp[i][j] = left if left[1] > right[1] else right
        
        # return dp[0][n][0] > dp[0][n][1] 



