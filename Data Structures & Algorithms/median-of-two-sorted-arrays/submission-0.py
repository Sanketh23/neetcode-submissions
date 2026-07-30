class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1) - 1

        while True:
            mid = (l + r) // 2
            two = half - mid - 2

            Aleft = nums1[mid] if mid >= 0 else float("-inf")
            Aright = nums1[mid+1] if (mid + 1) < len(nums1) else float("inf")
            Bleft = nums2[two] if two >= 0 else float("-inf")
            Bright = nums2[two+1] if (two + 1) < len(nums2) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                r = mid - 1
            elif Bleft > Aright:
                l = mid + 1
                


