class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def decreasing(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
            
            return True
        def increasing(nums):
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
            
            return True
        return increasing(nums) or decreasing(nums)
        
