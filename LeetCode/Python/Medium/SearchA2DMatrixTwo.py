class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) < 1:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while (row < len(matrix) and col > -1):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False