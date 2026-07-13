class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i, num in enumerate(nums):
            if nums[i-1] > num:
                count += 1
        
        if count > 1:
            return False
        return True
