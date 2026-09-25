class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        pacific, atlantic = set(), set()


        def dfs(r, c, visited, height):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < height or (r,c) in visited:
                return
            visited.add((r,c))
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols-1])
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows-1][c])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        
        return res
        
