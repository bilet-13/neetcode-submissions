class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            a, b = equations[i]

            graph[a][b] = values[i]
            graph[b][a] = 1 / values[i]

        for k in graph:
            for i in graph:
                for j in graph:
                    if k in graph[i] and j in graph[k]:
                        val = graph[i][k] * graph[k][j]

                        if j not in graph[i]:
                            graph[i][j] = val
        
        result = []
        for c, d in queries:
            if c in graph and d in graph[c]:
                result.append(graph[c][d])
            else:
                result.append(-1.0)
        return result
                

