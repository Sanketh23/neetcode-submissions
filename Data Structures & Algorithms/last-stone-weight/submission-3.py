class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        stones = [-s for s in stones]
        for stone in stones:
            heapq.heappush(heap, stone)
        while len(heap) > 1:
            largest = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if largest != second:
                heapq.heappush(heap, largest - second)
                print(heap)
                
        
        return abs(heap[0])

