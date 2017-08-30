class Solution(object):
    def countBattleships(self, board):
        if len(board) == 0 or len(board[0]) == 0:
            return 0

        rows = len(board)
        cols = len(board[0])

        count = 0
        for col in range(cols):
            for row in range(rows):
                if board[row][col] == 'X':
                    self.dfs(board, row, col)
                    count += 1

        return count

    def dfs(self, board, row, col):
        if row < 0 or row > len(board) - 1:
            return
        if col < 0 or col > len(board[0]) - 1:
            return

        if board[row][col] == '.':
            return

        board[row][col] = 'x'

        self.dfs(board, row + 1, col)
        self.dfs(board, row, col + 1)

        return
