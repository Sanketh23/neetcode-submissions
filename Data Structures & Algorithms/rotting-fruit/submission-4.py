from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        minutes = 0
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        if fresh == 0:
            return 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
                        if fresh == 0:
                            return minutes + 1
            minutes += 1
                    
        return -1
                    
                
        
        

