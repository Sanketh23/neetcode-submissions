class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(depth):
            if depth >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[depth])
            dfs(depth+1)
            path.pop()
            dfs(depth+1)

        dfs(0)
        return res
