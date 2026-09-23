class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l, r = 0, 0
        currProduct = nums[0]
        count = 0
        while r < len(nums):
            if currProduct < k:
                count += (r - l + 1)
                r += 1
                if r == len(nums):
                    return count
                else:
                    currProduct *= nums[r]
            else:
                currProduct /= nums[l]
                l += 1
                if l == len(nums):
                    return count

        