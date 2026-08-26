class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if (j - i) <= nums[i] and j < len(nums):
                    dp[j] = min(dp[i] + 1, dp[j])
    
        return dp[-1]