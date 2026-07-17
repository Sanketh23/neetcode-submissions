class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        upper = num // 2
        lower = 1
        while lower <= upper:
            mid = (lower+upper) // 2
            if mid * mid == num:
                return True
            elif mid*mid > num:
                upper = mid - 1
            else:
                lower = mid + 1
        
        return False