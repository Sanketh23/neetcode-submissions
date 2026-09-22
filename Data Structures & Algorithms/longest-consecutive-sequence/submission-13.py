class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashTable = Counter(nums)
        maxLen = float('-inf')
        curr = 1
        for start in nums:
            while start + 1 in hashTable:
                curr += 1
                start += 1
            maxLen = max(curr, maxLen)
            curr = 1
        return 0 if maxLen == float('-inf') else maxLen