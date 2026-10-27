class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            j = 0 
            k = len(matrix[i]) - 1
            while j <= k:
                mid = (j + k) // 2 
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target :
                    k = k - 1
                else :
                    j = j + 1
        return False 