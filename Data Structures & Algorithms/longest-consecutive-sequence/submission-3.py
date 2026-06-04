class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longest = 1
        current = 1
        numSet = set(nums)

        for i in range(len(nums)):
            if (nums[i] + 1) in numSet:
                current += 1
                longest = max(current, longest)
            else:
                current = 1
            
        
        return longest + 1

