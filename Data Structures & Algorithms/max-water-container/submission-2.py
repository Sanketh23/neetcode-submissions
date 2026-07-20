class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        area = 0
        while l <= r:
            area = (r-l) * min(heights[r],heights[l])
            maxArea = max(area, maxArea)
            if l > r:
                r -= 1
            else:
                l += 1
        
        return maxArea