class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n) ] for _ in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                num_possible_path = 0
                num_possible_path += dp[i - 1][j] if i - 1 >= 0 else 0
                num_possible_path += dp[i][j - 1] if j - 1 >= 0 else 0
                dp[i][j] = num_possible_path

        return dp[m - 1][n - 1]
        