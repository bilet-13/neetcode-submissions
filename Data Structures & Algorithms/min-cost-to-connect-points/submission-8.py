class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum spanning tree
        # prim
        # dense graph -> prim

        visited = set() 
        min_heap = [(0, 0)]
        min_cost = 0

        while len(visited) < len(points):
            dist, u = heapq.heappop(min_heap)

            if u in visited:
                continue

            visited.add(u)
            min_cost += dist

            for i in range(len(points)):
                if i in visited:
                    continue
                heapq.heappush(min_heap, (abs(points[u][0] - points[i][0]) + abs(points[u][1] - points[i][1]), i))
        
        return min_cost


            




        