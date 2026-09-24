class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()

        def dfs(r, c, curr):
            nonlocal maxArea
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r, c) in visited:
                return
            visited.add((r, c))
            if curr > maxArea:
                maxArea = curr
            for dr, dc in directions:
                dfs(r + dr, c + dc, curr + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c, 1)

        return maxArea