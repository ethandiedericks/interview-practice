import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = []
    
        for index, row in enumerate(mat):
            soldier_count = sum(row)
            heapq.heappush(min_heap, (soldier_count, index))
        
        weakest_rows = [heapq.heappop(min_heap)[1] for _ in range(k)]
        
        return weakest_rows