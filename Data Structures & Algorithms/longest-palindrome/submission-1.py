class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        hasOdd = False

        for c in count:
            if count[c] % 2 == 0:
                res += (count[c])
            else:
                res += (count[c] // 2) * 2
                hasOdd = True
    
        return res + 1 if hasOdd else res