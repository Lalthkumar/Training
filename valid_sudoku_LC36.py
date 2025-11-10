import sys
import json
import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # Key will be (r // 3, c // 3)

        for r in range(9):
            for c in range(9):
                char = board[r][c]
                if char == ".":
                    continue
                if (char in rows[r] or 
                    char in cols[c] or 
                    char in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(char)
                cols[c].add(char)
                squares[(r // 3, c // 3)].add(char)
        return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_sudoku.py '<json_board>'")
        sys.exit(1)

    board = json.loads(sys.argv[1])
    sol = Solution()
    print(sol.isValidSudoku(board))
