class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1,max2,min1,min2 = 0,0,float('inf'),float('inf')
        for i in nums:
            if i > max1:
                temp = max1
                max1 = i
                max2 = temp
            elif i > max2:
                max2 = i
            if i < min1:
                temp = min1
                min1 = i
                min2 = temp
            elif i < min2:
                min2 = i
        
        return (max1*max2) - (min1*min2)