class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin = 1
        curMax = 1

        for num in nums:
            temp = curMax * num
            curMax = max(temp, num * curMin)
            curMin = min(temp, num * curMax)

            res = max(res, curMax)
        
        return res