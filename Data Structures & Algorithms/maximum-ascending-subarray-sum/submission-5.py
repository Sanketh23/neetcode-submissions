class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = 0
        l,r = 0, 1
        while nums[l] > nums[r] and r <= len(nums):
            l += 1
            r += 1
        if r == len(nums) + 1:
            return max(nums)
        curr_sum = nums[l]
        while r < len(nums):
            if nums[r] > nums[l]:
                curr_sum += nums[r]
                r += 1
                l += 1
            else:
                r += 1
                l += 1
                curr_sum = nums[l]
            if curr_sum > maxSum:
                maxSum = curr_sum
        return maxSum