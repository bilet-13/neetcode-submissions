class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # uj is a prerequisite of vj equal to there is a path from uj to vj
        # node: course edge: uj to vj if uj is a prerequisite
        # so for each query, use dfs or bfs check if there is a path
        # tiem complexity o(len(queries) * (V + E)) = o(len(queries) * (numcourses + len(prereqruisite)))
        graph = [[] for i in range(numCourses)]

        for u, v in prerequisites:
            graph[u].append(v)

        def can_reach(start, end):
            stack = [start]
            visited = set(stack)

            while stack:
                course = stack.pop()
                
                if course == end:
                    return True
                
                for next_course in graph[course]:
                    if next_course not in visited:
                        visited.add(next_course) 
                        stack.append(next_course)

            return False

        result = []

        for uj, vj in queries:
            result.append(can_reach(uj, vj))
        
        return result
        
