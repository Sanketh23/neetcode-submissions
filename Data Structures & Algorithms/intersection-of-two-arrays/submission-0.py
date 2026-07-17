from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)

        maxLen = max(len(nums1), len(nums2))
        res = []
        if len(nums1) >= len(nums2):
            for i in count2.keys():
                if i in nums1:
                    if i not in res:
                        res.append(i)
        else:
            for i in count1.keys():
                if i in nums2:
                    if i not in res:
                        res.append(i)
            
        return res