from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        q = deque()

        def nextCell(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == -1:
                return
            visited.add((r,c))
            q.append([r,c])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c])
     
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                for dr, dc in directions:
                    nextCell(r + dr, c + dc)
            dist += 1

                    
                
        
        

