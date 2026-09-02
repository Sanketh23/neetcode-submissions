class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(depth):
            if depth >= len(nums):
                if sorted(path) in res:
                    return
                res.append(path.copy())
                return
            path.append(nums[depth])
            dfs(depth+1)
            path.pop()
            dfs(depth+1)

        dfs(0)
        return res