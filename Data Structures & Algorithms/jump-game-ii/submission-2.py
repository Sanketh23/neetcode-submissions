class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        count = 0
        while r < len(nums) - 1:
            farthest = max(r + nums[r], l + nums[l])
            count += 1
            print(farthest)
            if farthest >= len(nums) - 1:
                return count
            l = r + 1
            r = farthest
        
        return 0