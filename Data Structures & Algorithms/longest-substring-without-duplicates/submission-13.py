class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(set(s)) == 1:
            return 1
        maxLen = float('-inf')
        l, r = 0, 1
        hashSet = set()
        hashSet.add(s[l])

        while r < len(s):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            r += 1
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen - 1
        

