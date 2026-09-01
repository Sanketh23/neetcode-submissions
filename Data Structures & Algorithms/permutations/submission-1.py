class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        used = [False] * len(nums)
        def backtrack():
            if len(sol) == len(nums):
                res.append(sol.copy())
            for i, n in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    sol.append(n)
                    backtrack()
                    sol.pop()
                    used[i] = False
        
        backtrack()
        return res 