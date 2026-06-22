from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = {}
        maxLen = 0 
        l = 0

        for r in range(len(s)):
            if s[r] in hashSet:
                l = max(hashSet[s[r]] + 1, l)
            hashSet[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
            
        return maxLen
