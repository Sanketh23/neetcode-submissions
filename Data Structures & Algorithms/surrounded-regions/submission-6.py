from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        visited = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and ((r == 0 or r == rows - 1) or (c == 0 or c == cols - 1)):
                    visited.add((r,c))
                    q.append([r,c])
        
        def bfs(r,c):
            if r <= 0 or c <= 0 or r >= rows - 1 or c >= cols - 1 or (r,c) in visited or board[r][c] == 'X':
                return
            visited.add((r,c))
            q.append([r,c])
            board[r][c] = 'T'
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                bfs(r + dr, c + dc)
        
        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
        

