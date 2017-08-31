class Solution(object):
    def findCircleNUm(self, M):
        if len(M) == 0:
            return 0

        count = 0
        for i in range(len(M)):
            for j in range(len(M[0])):
                if M[i][j] == 1:
                    self.dfs(M, i, j)
                    count += 1

        return count

    def dfs(self, M, row, col):
        if row < 0 or row > len(M):
            return
        if col < 0 or col > len(M[0]):
            return

        if M[row][col] == 0:
            return

        M[row][col] = M[col][row] = 0

        for i in range(len(M)):
            self.dfs(M, row, i)
            self.dfs(M, i, col)

        return
