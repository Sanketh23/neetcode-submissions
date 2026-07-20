class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1set = set(nums1)
        num2set = set(nums2)
        res = [[],[]]

        for num in num1set:
            if num not in num2set:
                res[0].append(num)
        for num in num2set:
            if num not in num1set:
                res[1].append(num)
        
        return res
        

