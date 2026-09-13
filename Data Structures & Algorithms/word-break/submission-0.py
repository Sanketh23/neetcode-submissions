class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l, r = 0, 1
        count = 0
        while r < len(s):
            if s[l:r+1] in wordDict:
                l = r + 1
                r = l + 1
                count += 1
            r += 1
        
        if count == len(wordDict):
            return True
        return False