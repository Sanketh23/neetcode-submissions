class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum = 0
        current = nums[0]
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                current += nums[i+1]
                maximum = max(current, maximum)
            else:
                current = nums[i+1]
        return maximum
