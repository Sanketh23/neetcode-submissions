class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashMap = {i: 0 for i in range(1, len(nums) + 1)}
        res = []
        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        
        for i in hashMap.keys():
            if hashMap[i] == 0:
                res.append(i)

        
        return res