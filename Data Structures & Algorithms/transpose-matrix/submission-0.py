class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [[0] * len(matrix) for i in range(len(matrix[0]))]
        for r in range(len(matrix[0])):
            for c in range(len(matrix)):
                res[r][c] = matrix[c][r]
        
        return res