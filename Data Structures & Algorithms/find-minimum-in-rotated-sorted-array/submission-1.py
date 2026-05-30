class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, 1
        while nums[l] <= nums[r]:
            r += 1
            if nums[r] < nums[l] and r <= len(nums) - 1:
                return nums[r]
