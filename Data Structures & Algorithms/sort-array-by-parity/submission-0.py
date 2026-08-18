class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenIndex = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[evenIndex] = nums[evenIndex], nums[i]
                evenIndex += 1
        return nums