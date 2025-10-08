class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        return not stack

# Command-line interface
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python valid_parentheses.py \"<parentheses_string>\"")
    else:
        input_str = sys.argv[1]
        sol = Solution()
        result = sol.isValid(input_str)
        print(f"Input: {input_str}")
        print(f"Is valid? {result}")
