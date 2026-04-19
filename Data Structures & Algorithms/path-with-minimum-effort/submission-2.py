class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # minimum effort -> dijkstra

        min_cost = [[float("inf") for j in range(len(heights[0]))] for i in range(len(heights))]
        min_cost[0][0] = 0

        min_heap = [(0, 0, 0)] # effort, row, col
        n = len(heights)
        m = len(heights[0])

        while min_heap:
            effort, x, y = heapq.heappop(min_heap)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy
                
                if n > nx >= 0 and m > ny >= 0:
                    n_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                    if n_effort < min_cost[nx][ny]:
                        min_cost[nx][ny] = n_effort
                        heapq.heappush(min_heap, (n_effort, nx, ny))

        return min_cost[n - 1][m - 1]
        