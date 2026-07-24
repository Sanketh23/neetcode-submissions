class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0

        for c in count:
            if count[c] > 1:
                if count[c] % 2 == 0:
                    res += count[c]
                else:
                    res += (count[c] // 2) + 1
    
        return res + 1