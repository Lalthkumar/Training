import sys
import json

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        def is_valid(row, col, char):
            for i in range(9):
                if board[row][i] == char or board[i][col] == char:
                    return False
            start_row = (row // 3) * 3
            start_col = (col // 3) * 3
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == char:
                        return False
            return True

        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num_char in "123456789":
                            if is_valid(r, c, num_char):
                                board[r][c] = num_char
                                if solve():
                                    return True
                                board[r][c] = '.'
                        return False
            return True

        solve()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sudoku_solver.py '<json_board>'")
        sys.exit(1)

    board = json.loads(sys.argv[1])
    Solution().solveSudoku(board)

    for row in board:
        print(" ".join(row))
