class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        repeat = 0
        for num in nums:
            count[num] += 1
            if count[num] == 2:
                repeat = num
        n = len(nums)
        missing = 0
        missing = (n * (n+1))/2 - sum(nums) + repeat

        return [repeat,int(missing)]