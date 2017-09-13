class Solution(object):
    def isValidSudoku(self, board):
        for i in range(len(board)):
            vr = self.validRow(board, i)

            vc = self.validCol(board, i)

            vs = self.validSquare(board, i)

            if not vr or not vc or not vs:
                return False

        return True

    def validRow(self, board, row):
        seen = []
        for i in range(len(board)):
            if board[row][i] == '.':
                continue
            if board[row][i] not in seen:
                seen.append(board[row][i])
            else:
                return False
        return True

    def validCol(self, board, col):
        seen = []
        for i in range(len(board)):
            if board[i][col] == '.':
                continue
            if board[i][col] not in seen:
                seen.append(board[i][col])
            else:
                return False
        return True

    def validSquare(self, board, square):
        seen = []
        rowStart = (square / 3) * 3
        colStart = (square % 3) * 3
        for i in range(colStart, colStart + 3):
            for j in range(rowStart, rowStart + 3):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in seen:
                    seen.append(board[j][i])
                else:
                    return False
        return True
