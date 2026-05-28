from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        tab = Counter(nums)

        max_heap = [(-val, key) for key, val in tab.items()]
        heapq.heapify(max_heap)

        res = []

        for i in range(k):

            v1, k1 = heapq.heappop(max_heap)
            res.append(k1)
        
        return res


        
        