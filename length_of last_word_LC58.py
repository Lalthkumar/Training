import sys

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        last_word_end_index = i
        while i >= 0 and s[i] != ' ':
            i -= 1
        return last_word_end_index - i

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python last_word_length.py \"your input string\"")
    else:
        input_str = sys.argv[1]
        sol = Solution()
        print(sol.lengthOfLastWord(input_str))
