# filename: strstr_cli.py

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        len_hay, len_ndl = len(haystack), len(needle)

        for i in range(len_hay - len_ndl + 1):
            if haystack[i:i + len_ndl] == needle:
                return i

        return -1

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python strstr_cli.py <haystack> <needle>")
    else:
        haystack = sys.argv[1]
        needle = sys.argv[2]
        sol = Solution()
        result = sol.strStr(haystack, needle)
        print(f"Index of first occurrence: {result}")
