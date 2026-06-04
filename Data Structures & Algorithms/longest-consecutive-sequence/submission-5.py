class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        sorted_nums = sorted(nums)
        longest = 0
        current = 0
        numSet = set(nums)

        for i in range(len(sorted(nums))):
            if (sorted_nums[i] + 1) in numSet:
                current += 1
                longest = max(current, longest)
            else:
                current = 1
            
        
        return longest

