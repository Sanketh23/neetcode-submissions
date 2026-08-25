class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        def dfs(r,c):
            if r <= 0 or r >= rows - 1 or c <= 0 or c >= cols - 1 or (r,c) in visited:
                return
            visited.add((r,c))
            if board[r][c] == 'O':
                board[r][c] = 'X'

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X' and ((r == 0 or r == rows - 1) or (c == 0 or c == cols - 1)):
                    for dr, dc in directions:
                        dfs(r + dr, c + dc)
