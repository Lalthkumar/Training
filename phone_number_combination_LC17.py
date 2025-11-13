class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        result = []

        def backtrack(combination, next_digits):
            if not next_digits:
                result.append(combination)
                return

            digit = next_digits[0]
            letters = phone_map[digit]
            for letter in letters:
                backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        return result

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python solution.py <digits>")
        sys.exit(1)

    digits = sys.argv[1]
    sol = Solution()
    combinations = sol.letterCombinations(digits)
    print(combinations)
