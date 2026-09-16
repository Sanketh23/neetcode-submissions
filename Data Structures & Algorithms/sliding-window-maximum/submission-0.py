import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []

        maxHeap = []
        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            if r >= k - 1:
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                res.append(-1 * maxHeap[0][0])
                l += 1



        return res
        
