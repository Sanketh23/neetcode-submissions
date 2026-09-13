class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        charSet = set()
        l = 0
        charSet.add(s[l])
        r = 1
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            r += 1
            maxLen = max(maxLen, r - l)
        
        return maxLen