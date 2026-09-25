class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = dp.copy()
            for t in dp:
                nextDP.add(t + nums[i])
            dp = nextDP
        
        if target in dp:
            return True
        return False