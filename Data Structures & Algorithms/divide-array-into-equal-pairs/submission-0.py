from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count_nums = Counter(nums)

        for i in count_nums.keys():
            if count_nums[i] % 2 != 0:
                return False

        return True