class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []
        curr = 0
        for char in s:
            if char == '(':
                stack.append('(')
            elif char == ')':
                res = max(res, len(stack))
                stack.pop()
        
        return res
