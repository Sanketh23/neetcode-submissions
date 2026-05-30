class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "#"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            hashIndex = s.index("#", i)
            res.append(s[i:hashIndex])
            i = hashIndex + 1
        
        return res

