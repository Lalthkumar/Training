class Solution:
    def longestPalindrome(self, S: str) -> str:
        start = 0
        maxLen = 1
        for i in range(1, len(S)):
            # even
            l = i - 1
            r = i
            while l >= 0 and r < len(S) and S[l] == S[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    start = l
                l -= 1
                r += 1
            # odd
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(S) and S[l] == S[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    start = l
                l -= 1
                r += 1
        return S[start:start + maxLen]

# Example usage
if __name__ == "__main__":
    s = Solution()
    input_str = input("Enter a string: ")
    print("Longest Palindromic Substring:", s.longestPalindrome(input_str))
