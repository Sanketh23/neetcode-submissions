class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == ""):
            return 0
        l,r = 0,1
        length = 1
        max_len = 1
        hashset = set()

        while r < len(s):
            if s[l] != s[r] and s[r] not in hashset:
                hashset.add(s[r])
                length += 1
                max_len = max(length, max_len)
                r += 1
            else:
                hashset.clear()
                length = 1
                l += 1
                r = l + 1
        return max_len