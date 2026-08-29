import heapq
class MedianFinder:

    def __init__(self):
        self.numHeap = []
        heapq.heapify(self.numHeap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.numHeap, num)

    def findMedian(self) -> float:
        n = len(self.numHeap)
        if n == 1:
            return self.numHeap[0]
        elif n == 2:
            return ((self.numHeap[0]) + (self.numHeap[1])) / 2
        if n % 2 == 0:
            mid = n // 2
            median = ((self.numHeap[mid] + self.numHeap[mid + 1]) / 2)
            return median
        else:
            print(self.numHeap)
            return self.numHeap[n//2]
        