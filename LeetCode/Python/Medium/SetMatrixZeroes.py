class Solution(object):
    def setZeroes(self, matrix):
        if (len(matrix) < 1 or len(matrix[0]) < 1):
            return
        isFirstRow = False
        isFirstCol = False

        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                isFirstRow = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isFirstCol = True
                break

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                self.zeroOutCol(matrix, i, 1)

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                self.zeroOutRow(matrix, i, 1)

        if isFirstRow:
            self.zeroOutRow(matrix, 0, 0)

        if isFirstCol:
            self.zeroOutCol(matrix, 0, 0)
        return

    def zeroOutCol(self, matrix, col, start):
        for i in range(start, len(matrix)):
            matrix[i][col] = 0
        return

    def zeroOutRow(self, matrix, row, start):
        for i in range(start, len(matrix[0])):
            matrix[row][i] = 0
        return
