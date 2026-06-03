from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       count = Counter(nums)
       return (max(count.values()) > 1) 