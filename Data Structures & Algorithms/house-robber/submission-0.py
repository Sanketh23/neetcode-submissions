class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]

        max_money = 0
        
        for i in range(2, len(nums)):
            dp[i] = dp[i-2] + nums[i]
            max_money = max(max_money, dp[i])
        
        return max_money
