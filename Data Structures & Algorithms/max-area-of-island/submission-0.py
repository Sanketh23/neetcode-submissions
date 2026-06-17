class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        maxArea = 0
        current = 1

        def dfs(r,c):
            if (r,c) in visited:
                return 0
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            area = 1
            visited.add((r,c))
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            return area
        
        for r in range(rows):
            for c in range(cols):
                maxArea = max(dfs(r,c), maxArea)
        
        return maxArea