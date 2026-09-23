class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
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
                l += 1
                if l == len(nums):
                    return count
                currProduct = nums[l]

        