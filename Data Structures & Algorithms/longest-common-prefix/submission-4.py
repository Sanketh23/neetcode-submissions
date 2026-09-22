class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minLen = float('inf')
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        
        for i in range(minLen):
            for s in strs:
                if s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res