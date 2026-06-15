from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s1_len = len(s1)
        l = 0
        
        for r in range(s1_len - 1, len(s2)):
            count = Counter(s2[l:r+1])
            if count == s1_count:
                return True
            l += 1
            r += 1
        return False
                
            