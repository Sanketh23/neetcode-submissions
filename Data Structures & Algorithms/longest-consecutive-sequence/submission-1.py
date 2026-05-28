class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for i in nums:
            length = 1
            while i + 1 in nums:
                length += 1
                i+=1
            longest = max(length, longest)
        return longest