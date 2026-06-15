class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        first = 0
        maxFreq = 0
        for second in range(len(s)):
            count[s[second]] = 1 + count.get(s[second], 0)
            maxFreq = max(maxFreq, count[s[second]])

            while (second - first + 1) - maxFreq > k:
                count[s[first]] -= 1
                first += 1
            res = max(res, second - first + 1)
        
        return res
                