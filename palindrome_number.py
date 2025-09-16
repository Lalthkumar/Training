import sys

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python palindrome_check.py <integer>")
    else:
        num = int(sys.argv[1])
        sol = Solution()
        result = sol.isPalindrome(num)
        print(f"{num} is a palindrome: {result}")
