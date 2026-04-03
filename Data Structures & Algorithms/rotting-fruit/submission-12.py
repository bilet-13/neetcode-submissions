class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs 
        # queue element(pos_x, pos_y, time)
        # start with rotten fruits polluite the fresh fruite
        # store teh max time and make sure all fresh fruit are
        # rotten
        # time complexity o(n * m)

        queue = deque()
        fresh_num = 0
        fresh_become_rotten_num = 0
        max_time = 0

        n = len(grid)
        m = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh_num += 1

        while queue:
            x, y, time = queue.popleft()
            max_time = max(max_time, time)

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if n > nx >= 0 and m > ny >= 0 and grid[nx][ny] == 1:
                    grid[nx][ny] = 2 
                    fresh_become_rotten_num += 1
                    queue.append((nx, ny, time + 1))
        
        return max_time if fresh_become_rotten_num == fresh_num else -1



        