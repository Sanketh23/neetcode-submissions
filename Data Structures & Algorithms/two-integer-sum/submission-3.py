class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            if target - nums[i] in hashSet:
                return [hashSet[target-nums[i]], i]
            hashSet[nums[i]] = i
        