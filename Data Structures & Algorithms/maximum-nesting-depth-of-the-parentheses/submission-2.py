class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curr = 0
        for char in s:
            if char == '(':
                curr += 1
            elif char == ')':
                res = max(res, curr)
                curr -= 1

        
        return res
            
