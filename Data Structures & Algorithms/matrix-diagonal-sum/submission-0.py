class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res, n = 0, len(mat)
        if n==0:
            return 0
        for r in range(n):
            res += mat[r][r]
            res += mat[r][n-r-1]

        if n%2==1:
            return res - (mat[n//2][n//2])
        else:
            return res