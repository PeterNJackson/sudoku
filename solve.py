import argparse
from sudoku import Sudoku
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-pf", "--puzzleFile", required=False, default="/home/peter/PycharmProjects/sudoku/puzzle.txt",
                help="Puzzle file")
args = vars(ap.parse_args())

# read board from the puzzle.txt file
f = open(args["puzzleFile"], "r")
listIt = []
fulList = []
for i in range(0, 9):
    line = f.readline()
    for j in range(0, 9):
        listIt.append(int(line[j]))
    fulList.append(listIt)
    listIt = []

board = np.array(fulList)

# construct a sudoku puzzle from the board
print("[INFO] Sudoku board:")
puzzle = Sudoku(3, 3, board=board.tolist())
puzzle.show()

# solve the sudoku puzzle
print("[INFO] solving sudoku puzzle...")
solution = puzzle.solve()

solution.show_full()
