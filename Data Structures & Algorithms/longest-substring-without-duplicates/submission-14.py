class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s is empty
        if s == "":
            return 0
        if len(set(s)) == 1:
            return 1
        maxLen = float('-inf')
        hashSet = set()
        l = 0
        for r in range(len(s)):
            while s[r] in hashSet:
                hashSet.remove(s[l])
                l += 1
            hashSet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
        return maxLen

        

