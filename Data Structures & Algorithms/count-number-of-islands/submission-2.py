class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        count = 0
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    r,c = dr + row, dc + col
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == '1' and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    count += 1
        
        return count
