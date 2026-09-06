class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def dfs(i):
            if i == len(s):
                res.append(sol.copy())
                return
            for j in range(i, len(s)):
                temp = s[i:j+1]
                if temp == temp[::-1]:
                    sol.append(s[i:j+1])
                    dfs(j+1)
                    sol.pop()
            

        dfs(0)
        return res