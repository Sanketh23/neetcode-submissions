class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                for dr, dc in directions:
                    if r + dr < 0 or c + dc < 0 or r + dr >= rows or c + dc>= cols or (r+dr,c+dc) in visited or grid[r+dr][c+dc] == -1:
                        continue
                    visited.add((r+dr,c+dc))
                    q.append((r+dr,c+dc))
            distance += 1



        