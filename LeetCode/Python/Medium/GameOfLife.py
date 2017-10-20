class Solution:
    def gameOfLife(self, board):
        for row in range(len(board)):
            for col in range(len(board[0])):
                lives = self.countLiveNeighbors(board, row, col)
                if board[row][col] == 0 and lives == 3:
                    board[row][col] = 2
                elif board[row][col] == 1 and 2 <= lives <= 3:
                    board[row][col] = 3

        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] >>= 1
        return

    def countLiveNeighbors(self, board, row, col):
        lives = 0

        for i in range(max(row - 1, 0), min(row + 1, len(board) - 1) + 1):
            for j in range(max(col - 1, 0), min(col + 1, len(board[0]) - 1) + 1):
                print i, j
                lives += board[i][j] & 1
        lives -= (board[row][col] & 1)
        print " "
        return lives
