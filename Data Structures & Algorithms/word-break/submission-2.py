class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == wordDict[0]:
            return True
        l, r = 0, 0
        count = 0
        while r < len(s):
            if l == r:
                if s[l] in wordDict:
                    l = r + 1
                    r = l + 1
                    count += 1
                else:
                    r += 1
            if s[l:r+1] in wordDict:
                l = r + 1
                r = l + 1
                count += 1
            r += 1
        
        if count == len(wordDict):
            return True
        return False