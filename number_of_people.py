import sys

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        new = [0] * (n + 1)
        new[1] = 1
        for day in range(1, n+1):
            share = new[day]
            start = day + delay
            end = day + forget
            for nxt in range(start , min(end, n+1)):
                new[nxt] = (new[nxt] + share) % MOD
        ans = 0
        for day in range(n - forget +1, n+1):
            if day > 0:
                ans = (ans + new[day]) % MOD
        return ans

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python secret_spread.py <n> <delay> <forget>")
    else:
        n = int(sys.argv[1])
        delay = int(sys.argv[2])
        forget = int(sys.argv[3])
        sol = Solution()
        print(sol.peopleAwareOfSecret(n, delay, forget))
