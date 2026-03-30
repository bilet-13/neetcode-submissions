class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # uj is a prerequisite of vj equal to there is a path from uj to vj
        # node: course edge: uj to vj if uj is a prerequisite
        # so for each query, use dfs or bfs check if there is a path
        # tiem complexity o(len(queries) * (V + E)) = o(len(queries) * (numcourses + len(prereqruisite)))

        # udpate version:
        # dp -> floyd warshl o(V^3)
        # hash map of set to sotre all prereq for course i X

        dp = [[False for _ in range(numCourses)] for _ in range(numCourses)]

        for a, b in prerequisites:
            dp[a][b] = True

        for i in range(numCourses):
            for j in range(numCourses):
                for k in range(numCourses):
                    dp[i][j] |= dp[i][k] & dp[k][j]
        
        result = []

        for u, v in queries:
            result.append(dp[u][v])
        
        return result


