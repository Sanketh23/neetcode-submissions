import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateEuclideanDistance(p1: List[List[int]]) -> int:
            return math.sqrt((p1[0])**2 + (p1[1])**2)
        minHeap = []
        heapq.heapify(minHeap)
        for point in points:
            heapq.heappush(minHeap, [calculateEuclideanDistance(point), point[0], point[1]])
        res = []
        i = 0
        while i < k:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            i += 1
        
        return res
            