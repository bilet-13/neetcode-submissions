class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # single source shortest problem
        # weight >= 0
        # dijkstra
        min_times = {i: float("inf") for i in range(1, n + 1)}
        min_times[k] = 0
        graph = defaultdict(list)
        
        for u, v, t in times:
            graph[u].append((v, t))

        min_heap = [(k, 0)]

        while min_heap:
            cur, cur_t = heapq.heappop(min_heap)

            for nbr, nbr_t in graph[cur]:
                if cur_t + nbr_t < min_times[nbr]:
                    min_times[nbr] = cur_t + nbr_t
                    heapq.heappush(min_heap, (nbr, cur_t + nbr_t))
        
        mini_maximum_time = max(t for t in min_times.values())
        return mini_maximum_time if mini_maximum_time != float("inf") else -1


        