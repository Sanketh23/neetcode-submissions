class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def backtrack(i):
            if i == len(s):
                return True
            
            for end in range(i + 1, len(s) + 1):
                if s[i:end] in wordDict:
                    if (backtrack(end)):
                        return True
            return False
                    
        return backtrack(0)
