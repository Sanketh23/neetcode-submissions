class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        hashSet = []
        def dfs(depth):

            if depth >= len(nums):
                count = Counter(path)
                if count in hashSet:
                    return
                res.append(path.copy())
                hashSet.append(count)
                return
            path.append(nums[depth])
            dfs(depth+1)
            path.pop()
            dfs(depth+1)

        dfs(0)
        return res