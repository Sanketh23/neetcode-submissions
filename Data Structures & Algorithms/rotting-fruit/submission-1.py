from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        q = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
        
        def checkAdjacent(r,c):
            nonlocal fresh
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == 0:
                return
            grid[r][c] = 2
            fresh -= 1
            visited.add((r,c))
            q.append((r,c))

        minutes = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    checkAdjacent(r + dr, c + dc)
                    
            minutes += 1
            if fresh == 0:
                return minutes
        return -1
                
        
        

