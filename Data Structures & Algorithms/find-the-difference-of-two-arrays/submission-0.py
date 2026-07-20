class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)

        for num, count in c1.items():
            if num in nums2:
                nums1[num] -= 1
                nums2[num] -= 1
        
        res = [[],[]]
        for num in nums1:
            res[0].append(num)
        for num in nums2:
            res[1].append(num)
        return res
        

