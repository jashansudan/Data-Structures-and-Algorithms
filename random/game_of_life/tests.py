import game_of_life
import concurrent_game_of_life
import copy


def simulationRuns(num, board):
    for i in range(num):
        board_copy = copy.deepcopy(board)
        game_of_life.GameOfLife.simulate(board)
        concurrent_game_of_life.GameOfLife.simulate(board_copy)
        if board == board_copy:
            print "Board is good"
        else:
            print "Board is bad"


board1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

board2 = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

for board in [board1, board2]:
    simulationRuns(5, board)
