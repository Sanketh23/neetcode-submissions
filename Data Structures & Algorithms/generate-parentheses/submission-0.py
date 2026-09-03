class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(Open, Close):
            if len(sol) == 2 * n:
                res.append("".join(sol))
            
            if Open < n:
                sol.append('(')
                backtrack(Open + 1, Close)
                sol.pop()
            
            if Open > Close:
                sol.append(')')
                backtrack(Open, Close + 1)
                sol.pop()
        
        backtrack(0, 0)
        return res