class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 1
        while s[r] == s[0]:
            r += 1
            if r == len(s):
                return 1
        l = r - 1
        curr = set()
        curr.add(s[l])
        curr.add(s[r])
        maxLen = 2
        r += 1
        while r < len(s):
            if s[r] in curr:
                maxLen = max(maxLen, r - l)
                curr.clear()
                l = r
                r += 1
                curr.add(s[l])
                if r == len(s):
                    return maxLen
                curr.add(s[r])
            r += 1
        return maxLen