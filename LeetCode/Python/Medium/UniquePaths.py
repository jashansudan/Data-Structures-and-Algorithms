class Solution(object):
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0

        grid = [[0 for i in range(n)] for i in range(m)]

        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]
