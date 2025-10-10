from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans, sol = []

        def backtrack(openn, close):
            if len(sol) == 2 * n:
                ans.append("".join(sol))
                return
            if openn < n:
                sol.append("(")
                backtrack(openn + 1, close)
                sol.pop()
            if openn > close:
                sol.append(")")
                backtrack(openn, close + 1)
                sol.pop()

        sol = []
        backtrack(0, 0)
        return ans

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python generate_parenthesis.py <n>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        solution = Solution()
        result = solution.generateParenthesis(n)
        print("Generated Parentheses:")
        for combo in result:
            print(combo)
    except ValueError:
        print("Please provide a valid integer for n.")
