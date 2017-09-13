class Solution(object):
    def numIslands(self, grid):
        if len(grid) < 1:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                    self.dfs(grid, i, j)

        return count

    def dfs(self, grid, row, col):
        if row < 0 or row > len(grid):
            return
        if col < 0 or col > len(grid[0]):
            return
        if grid[row][col] == 0:
            return

        grid[row][col] = 0

        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        return
