class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            mid = (l + r) //2
            hours = 0
            for i in range(len(piles)):
                hours += (piles[i] // mid) + 1 if (piles[i] % mid) != 0 else (piles[i] // mid)
            if hours <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res
