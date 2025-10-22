class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        prev = self.countAndSay(n - 1)
        result = ""
        count = 1

        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
            else:
                result += str(count) + prev[i]
                count = 1
        return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python count_and_say.py <n>")
    else:
        n = int(sys.argv[1])
        sol = Solution()
        print(sol.countAndSay(n))
