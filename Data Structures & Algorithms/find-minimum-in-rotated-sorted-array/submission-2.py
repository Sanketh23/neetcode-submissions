class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]
        while l <= r:
            m = (l+r)//2
            minimum = min(minimum, nums[m])
            if nums[l] <= nums[m]:
                l = m+1
            else:
                r = m-1
            
        return minimum