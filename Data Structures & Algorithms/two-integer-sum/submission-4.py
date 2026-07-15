class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            sub = target - num
            if sub in hashMap:
                return [hashMap[sub], i]
            hashMap[num] = i
        
