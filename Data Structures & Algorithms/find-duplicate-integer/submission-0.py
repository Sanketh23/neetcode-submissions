from collections import defaultdict
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = defaultdict(int)
        for num in nums:
            hashSet[num] += 1
            if hashSet[num] == 2:
                return num
                
        