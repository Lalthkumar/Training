import sys

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        i = 0
        d = 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[i].append(char)
            if i == 0:
                d = 1
            elif i == numRows - 1:
                d = -1
            i += d
        ret = ''
        for i in range(numRows):
            ret += ''.join(rows[i])

        return ret

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python zigzag_convert.py <string> <numRows>")
    else:
        s = sys.argv[1]
        numRows = int(sys.argv[2])
        sol = Solution()
        print(sol.convert(s, numRows))
