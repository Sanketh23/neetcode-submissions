class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxProduct = float('-inf')
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i] = max(dp[i-1], nums[i] * dp[i-1])
                maxProduct = max(dp[i], maxProduct)
            else:
                dp[i] = nums[i]

        return maxProduct