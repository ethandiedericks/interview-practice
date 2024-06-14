import heapq
from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        arr = []

        while nums:
            a, b = heapq.heappop(nums), heapq.heappop(nums)
            arr.append(b)
            arr.append(a)
        return arr