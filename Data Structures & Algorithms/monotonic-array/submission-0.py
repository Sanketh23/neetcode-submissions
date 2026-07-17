class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i = 1
        if nums[1] >= nums[0]:
            while i < len(nums):
                if nums[i] >= nums[i-1]:
                    i += 1
                else:
                    break
            if i == len(nums):
                return True
        elif nums[1] <= nums[0]:
            while i < len(nums):
                if nums[i] <= nums[i-1]:
                    i += 1
                else:
                    break
            if i == len(nums):
                return True
        
        return False
