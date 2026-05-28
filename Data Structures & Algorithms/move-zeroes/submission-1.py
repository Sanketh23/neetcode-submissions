class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nonZeroIndex] = nums[nonZeroIndex], nums[i]
                nonZeroIndex += 1
        