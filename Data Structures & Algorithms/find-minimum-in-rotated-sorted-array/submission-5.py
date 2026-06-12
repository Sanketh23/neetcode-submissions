class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        if len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if mid > l:
                l = mid + 1
            else:
                r = mid - 1

        return res