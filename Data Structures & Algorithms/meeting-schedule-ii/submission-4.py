"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []
        min_room = 0

        for interval in intervals:
            if not min_heap:
                heapq.heappush(min_heap, interval.end)
            
            else:
                if min_heap[0] <= interval.start:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, interval.end)
                else:
                    heapq.heappush(min_heap, interval.end)
            
            min_room = max(min_room, len(min_heap))

        return min_room

