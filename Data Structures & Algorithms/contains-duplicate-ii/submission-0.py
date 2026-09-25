class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashSet = defaultdict(int)

        for i, num in enumerate(nums):
            if num in hashSet:
                if abs(hashSet[num] - i) <= k:
                    return True
                else:
                    return False
            hashSet[num] = i
                
