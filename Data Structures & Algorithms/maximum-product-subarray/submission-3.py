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
            if nums[i] >= 0:
                possible_max = nums[i] * dp[i-1]
                possible_min = nums[i] * dp_negative[i-1]
            else:
                possible_max = nums[i] * dp_negative[i-1]
                possible_min = nums[i] * dp[i-1]  

            
            dp_negative[i] = min(nums[i], possible_min)
            dp[i] = max(nums[i], possible_max)
            maxProduct = max(maxProduct, dp[i])

        return max(dp)