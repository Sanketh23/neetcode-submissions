import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = [0] * (len(nums) - k + 1)

        maxHeap = []
        for r in range(len(nums)):
            heapq.heappush(maxHeap, (-nums[r], r))
            if r >= k - 1:
                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                res[l] = (-1 * maxHeap[0][0])
                l += 1



        return res
        
