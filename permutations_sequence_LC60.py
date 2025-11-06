import argparse
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        permutations = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutations += str(numbers[index])
            numbers.pop(index)
        return permutations

def main():
    parser = argparse.ArgumentParser(description="Get the k-th permutation of numbers 1 to n.")
    parser.add_argument("n", type=int, help="The upper bound of the number range (1 to n)")
    parser.add_argument("k", type=int, help="The k-th permutation to find")
    args = parser.parse_args()

    solution = Solution()
    result = solution.getPermutation(args.n, args.k)
    print(f"The {args.k}-th permutation of numbers 1 to {args.n} is: {result}")

if __name__ == "__main__":
    main()
