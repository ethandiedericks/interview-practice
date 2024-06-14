import heapq 
from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0

        while grid and grid[0]:
            max_heap = []
            for row in grid:
                biggest = max(row)
                heapq.heappush(max_heap, -biggest)
                row.remove(biggest)
            
            res += -heapq.heappop(max_heap)

        return res