class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def bfs(rows,cols):
            q = deque([(rows,cols)])
            visited.add((rows,cols))

            while q:
                rows, cols = q.popleft()
                if r >= 0 and r < (rows) or c >= 0 or c < (cols) or grid[r][c] == "1" or (r,c) not in visited:
                    grid[r][c] = "0"
                    for dr, dc in directions:
                        bfs(r + dr, c + dc)

        count = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    count += 1
        
        return count