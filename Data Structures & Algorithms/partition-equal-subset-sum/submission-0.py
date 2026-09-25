class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for curr in range(target, num - 1, -1):
                dp[curr] = dp[curr] or dp[curr - num]
        return dp[target]