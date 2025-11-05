import argparse

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_e = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char == '.':
                if seen_dot or seen_e:
                    return False
                seen_dot = True
            elif char in ('e', 'E'):
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False  # reset for exponent part
            elif char in ('+', '-'):
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
            else:
                return False
        return seen_digit

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if a string is a valid number.")
    parser.add_argument("input", type=str, help="String to validate as a number")
    args = parser.parse_args()

    sol = Solution()
    result = sol.isNumber(args.input)
    print(f"Is '{args.input}' a valid number? {result}")
