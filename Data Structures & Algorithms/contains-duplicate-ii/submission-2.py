class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        hashSet = defaultdict(int)

        for i, num in enumerate(nums):
            if num in hashSet:
                if abs(hashSet[num] - i) <= k:
                    return True
                
            hashSet[num] = i
        return False
                
