class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        upper = num // 2
        lower = 0
        while lower <= upper:
            mid = (lower+upper) // 2
            if mid * mid == num:
                return True
            elif mid*mid > num:
                upper = mid - 1
            else:
                lower = mid + 1
        
        return False