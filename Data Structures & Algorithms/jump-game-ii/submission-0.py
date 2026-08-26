class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if (j - i) <= nums[i]:
                    dp[j] = min(dp[i] + 1, dp[j])
    
                
        print(dp)
        return 0