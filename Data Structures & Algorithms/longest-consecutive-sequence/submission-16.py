class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        maxLen = float('-inf')
        for start in nums:
            if (start - 1) not in nums:
                curr = 1
                while start + curr in nums:
                    curr += 1
                maxLen = max(curr, maxLen)
        return 0 if maxLen == float('-inf') else maxLen