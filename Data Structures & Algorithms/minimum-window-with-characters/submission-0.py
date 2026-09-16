from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        if len(t) > len(s):
            return ""

        l = 0
        res = [0,0]
        minLen = float("inf")
        count_t = Counter(t)
        count_curr = defaultdict(int)
        curr, needed = 0, len(set(t))

        for r in range(len(s)):
            count_curr[s[r]] += 1
            if count_curr[s[r]] == count_t[s[r]]:
                curr += 1
            
            while curr == needed:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    res = [l,r]
                if s[l] in count_t.keys():
                    count_curr[s[l]] -= 1
                    curr -= 1
                    l += 1
                else:
                    count_curr[s[l]] -= 1
                    l += 1

                    
                    
        
        l = res[0]
        r = res[1]
        return s[l:r+1]

