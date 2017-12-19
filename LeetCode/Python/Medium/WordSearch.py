class Solution(object):
    def exist(self, board, word):
        visited = [[False for i in range(len(board[0]))] for i in range(len(board))]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    found = self.dfs(board, word, 0, visited, row, col)
                    if found:
                        return True
        return False

    def dfs(self, board, word, index, visited, row, col):
        if row < 0 or row >= len(board):
            return False
        if col < 0 or col >= len(board[0]):
            return False
        if visited[row][col]:
            return False
        if word[index] != board[row][col]:
            return False
        if index == len(word) - 1:
            return True

        visited[row][col] = True
        if self.dfs(board, word, index + 1, visited, row, col - 1) or self.dfs(board, word, index + 1, visited, row, col + 1) or self.dfs(board, word, index + 1, visited, row - 1, col) or self.dfs(board, word, index + 1, visited, row + 1, col)
            return True
        visited[row][col] = False
        return False