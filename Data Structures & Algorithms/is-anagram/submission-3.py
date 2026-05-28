class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        countS = {}
        countT = {}
        for l in s:
            countS[l] = 1 + countS.get(l, 0)
        for l in t:
            countT[l] = 1 + countT.get(l, 0)
        return countS == countT
