from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        count = Counter(nums)
        return (max(count.values()) > 1) 