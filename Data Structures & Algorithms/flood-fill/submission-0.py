class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current = image[sr][sc]
        if current == color:
            return image
        rows, cols = len(image), len(image[0])
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != current:
                return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        dfs(sr,sc)
        return image

        