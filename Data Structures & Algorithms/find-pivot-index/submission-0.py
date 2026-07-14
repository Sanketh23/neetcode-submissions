class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for r in range(len(nums)):
            right = total - nums[r] - left
            if left == right:
                return r
            left += nums[r]
        
        return -1
            