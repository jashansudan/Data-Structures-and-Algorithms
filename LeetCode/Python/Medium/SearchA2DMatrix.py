class Solution(object):
    def searchMatrix(self, matrix, target):
        if matrix is None or len(matrix) < 1:
            return False
        row = 0
        col = len(matrix[0]) - 1

        while (row < len(matrix) and col > -1):
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                row += 1
            else:
                col -= 1

        return False
