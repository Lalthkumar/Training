class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits

if __name__ == "__main__":
    import sys
    import ast

    if len(sys.argv) != 2:
        print("Usage: python plus_one.py \"[1,2,3]\"")
        sys.exit(1)

    input_digits = ast.literal_eval(sys.argv[1])
    sol = Solution()
    result = sol.plusOne(input_digits)
    print("Output:", result)
