class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # for node undefined return -1.0
        # pre-caculated the all pair shortest path
        # floyd warshell
        # time complexity o(V ^ 3)
        

        graph = defaultdict(list)
        idx = 0

        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def bfs(start, end):
            queue = deque()
            queue.append((start, 1))
            visited = set()
            visited.add(start)

            while queue:
                n, n_val = queue.popleft()

                if n == end:
                    return n_val

                for nbr , value in graph[n]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append((nbr, n_val * value))
            return -1.0

        result = []
        for c, d in queries:
            if c in graph:
                result.append(bfs(c, d))
            else:
                result.append(-1.0)
        
        return result