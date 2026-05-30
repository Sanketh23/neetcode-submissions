class Solution:
    def validPalindrome(self, s: str) -> bool:
        mistake = 0
        s = s.lower()
        l,r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                if mistake == 1:
                    return False
                if s[l] == s[r-1]:
                    r -= 1
                elif s[r] == s[l+1]:
                    l += 1
                mistake += 1
            l += 1
            r -= 1
        
        return True