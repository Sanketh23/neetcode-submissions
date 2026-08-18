class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nonValIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[nonValIndex] = nums[nonValIndex], nums[i]
                nonValIndex += 1
        
        return nonValIndex