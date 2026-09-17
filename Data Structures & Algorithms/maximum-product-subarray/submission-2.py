class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp_negative = [float('inf')] * len(nums)

        dp[0] = nums[0]
        dp_negative[0] = nums[0]

        maxProduct = float('-inf')

        for i in range(1, len(nums)):
            max_curr = max(nums[i] * dp[i-1], nums[i])
            dp_negative[i] = min(nums[i] * dp_negative[i-1], nums[i])
            dp[i] = max(max_curr, nums[i] * dp_negative[i-1])

        return max(dp)