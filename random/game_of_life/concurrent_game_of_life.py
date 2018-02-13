from threading import Thread


class GameOfLife:
    @staticmethod
    def simulate(board):
        all_threads = []
        for row in range(len(board)):
            thread = Thread(target=GameOfLife.gameOfLifeRow, args=[board, row])
            all_threads.append(thread)

        GameOfLife.awaitThreads(all_threads)

        all_threads = []

        for row in range(len(board)):
            thread = Thread(target=GameOfLife.shiftRow, args=[board, row])
            all_threads.append(thread)

        GameOfLife.awaitThreads(all_threads)

    @staticmethod
    def awaitThreads(all_threads):
        for t in all_threads:
            t.start()

        for x in all_threads:
            x.join()

    @staticmethod
    def gameOfLifeRow(board, row):
        for col in range(len(board[0])):
            ones = GameOfLife.countOnes(board, row, col)
            if board[row][col] and (ones == 2 or ones == 3):
                board[row][col] |= 2
            elif not board[row][col] and ones == 3:
                board[row][col] |= 2

    @staticmethod
    def shiftRow(board, row):
        for col in range(len(board[0])):
            board[row][col] >>= 1

    @staticmethod
    def countOnes(board, row, col):
        total = 0
        total += GameOfLife.isOne(board, row - 1, col - 1)
        total += GameOfLife.isOne(board, row - 1, col)
        total += GameOfLife.isOne(board, row - 1, col + 1)
        total += GameOfLife.isOne(board, row, col - 1)
        total += GameOfLife.isOne(board, row, col + 1)
        total += GameOfLife.isOne(board, row + 1, col - 1)
        total += GameOfLife.isOne(board, row + 1, col)
        total += GameOfLife.isOne(board, row + 1, col + 1)
        return total

    @staticmethod
    def isOne(board, row, col):
        if row >= len(board) or row < 0:
            return 0
        if col >= len(board) or col < 0:
            return 0
        return board[row][col] & 1
