class Solution:
    def maxKilledEnemies(self, grid):
        if not grid:
            return 0
        maxKilled = 0
        colEnemies = [-1] * len(grid[0])
        for row in range(len(grid)):
            rowEnemies = -1
            for col in range(len(grid[0])):
                if grid[row][col] == 'W':
                    rowEnemies = -1
                    colEnemies[col] = -1
                    continue
                if rowEnemies == -1:
                    rowEnemies = self.calculateRow(row, col, grid)
                if colEnemies[col] == -1:
                    colEnemies[col] = self.calculateCol(row, col, grid)
                if grid[row][col] == 'E':
                    continue
                maxKilled = max(maxKilled, rowEnemies + colEnemies[col])
        return maxKilled

    def calculateRow(self, row, col, grid):
        enemies = 0
        for i in range(col, len(grid[0])):
            if grid[row][i] == 'W':
                break
            elif grid[row][i] == 'E':
                enemies += 1
        return enemies

    def calculateCol(self, row, col, grid):
        enemies = 0
        for i in range(row, len(grid)):
            if grid[i][col] == 'W':
                break
            elif grid[i][col] == 'E':
                enemies += 1
        return enemies
