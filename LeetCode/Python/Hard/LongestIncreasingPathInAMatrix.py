class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0

        longest_path = 1
        path_length = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if path_length[row][col] != 0:
                    continue
                path = self.dfs(matrix, row, col, path_length, -1)
                longest_path = max(path, longest_path)

        return longest_path

    def dfs(self, matrix, row, col, path_length, prev):
        if row < 0 or row >= len(matrix):
            return 0
        if col < 0 or col >= len(matrix[0]):
            return 0

        if prev >= matrix[row][col]:
            return 0

        if path_length[row][col] != 0:
            return path_length[row][col]

        path_length[row][col] = 1
        prev = matrix[row][col]
        left_path = self.dfs(matrix, row, col - 1, path_length, prev)
        right_path = self.dfs(matrix, row, col + 1, path_length, prev)
        up_path = self.dfs(matrix, row + 1, col, path_length, prev)
        down_path = self.dfs(matrix, row - 1, col, path_length, prev)

        longest = max(max(left_path, right_path), max(up_path, down_path))
        path_length[row][col] = 1 + longest
        return 1 + longest
