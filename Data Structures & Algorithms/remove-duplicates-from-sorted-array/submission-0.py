class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while slow < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
                nums.remove(nums[fast])
            slow += 1
            fast += 1
        return len(nums)