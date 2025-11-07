import argparse

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

def main():
    parser = argparse.ArgumentParser(description="Calculate unique paths in an m x n grid.")
    parser.add_argument("m", type=int, help="Number of rows")
    parser.add_argument("n", type=int, help="Number of columns")
    args = parser.parse_args()

    solution = Solution()
    result = solution.uniquePaths(args.m, args.n)
    print(f"Unique paths for a {args.m}x{args.n} grid: {result}")

if __name__ == "__main__":
    main()
