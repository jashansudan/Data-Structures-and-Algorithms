class Solution:
    def spiralOrder(self, matrix):
        result = []
        if not matrix:
            return result
        rowBeg = 0
        rowEnd = len(matrix) - 1
        colBeg = 0
        colEnd = len(matrix[0]) - 1
        while rowBeg <= rowEnd and colBeg <= colEnd:

            for i in range(colBeg, colEnd + 1):
                result.append(matrix[rowBeg][i])

            rowBeg += 1

            for i in range(rowBeg, rowEnd + 1):
                result.append(matrix[i][colEnd])

            colEnd -= 1

            if rowBeg <= rowEnd:
                for i in range(colEnd, colBeg - 1, -1):
                    result.append(matrix[rowEnd][i])

                rowEnd -= 1

            if colBeg <= colEnd:
                for i in range(rowEnd, rowBeg - 1, -1):
                    result.append(matrix[i][colBeg])

                colBeg += 1

        return result
