class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(row: List[int]) -> bool:
            l, r = 0, len(row) - 1
            while l <= r:
                mid = (l + r) // 2
                if target == row[mid]:
                    return True
                elif target > row[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
            
        l,r = 0, len(matrix) - 1
        len_matrix = len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and matrix[mid][len_matrix] >= target:
                return(binarySearch(matrix[mid]))
               
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
            
        