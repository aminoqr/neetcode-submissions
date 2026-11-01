from collections import Counter, defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        counter = Counter(nums)
        heap = []
        for key, value in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (value, key))
            else:
                heapq.heappushpop(heap, (value, key))
        
        return [pair[1] for pair in heap]
        