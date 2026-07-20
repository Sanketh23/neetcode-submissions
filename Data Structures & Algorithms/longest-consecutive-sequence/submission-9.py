class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        hashTable = Counter(nums)
        maxLen = 1
        current = 1
        for num in nums:
            while num + 1 in hashTable:
                num = num + 1
                current += 1
            else:
                maxLen = max(maxLen, current)
                current = 1
        
        return maxLen