class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = Counter(nums)
        maxLen = 0
        current = 0
        for num in nums:
            while num + 1 in hashTable:
                num = num + 1
                current += 1
            else:
                maxLen = max(maxLen, current)
                current = 0
        
        return maxLen + 1