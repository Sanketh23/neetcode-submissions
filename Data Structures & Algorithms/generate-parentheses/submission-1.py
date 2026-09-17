class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []

        def backtrack(n, Open, Close):
            if len(sol) == 2 * n:
                res.append("".join(sol))
                return
            
            if Open < n:
                sol.append('(')
                backtrack(n, Open + 1, Close)
                sol.pop()
            
            if Open > Close:
                sol.append(')')
                backtrack(n, Open, Close + 1)
                sol.pop()

        
        backtrack(n,0,0)
        return res
