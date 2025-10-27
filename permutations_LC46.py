class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        current_permutation = []
        used = [False] * len(nums)

        def backtrack():
            if len(current_permutation) == len(nums):
                result.append(list(current_permutation))
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    current_permutation.append(nums[i])
                    backtrack()
                    current_permutation.pop()
                    used[i] = False

        backtrack()
        return result

# Command-line execution
if __name__ == "__main__":
    import sys
    input_nums = list(map(int, sys.argv[1:]))
    solution = Solution()
    permutations = solution.permute(input_nums)
    for p in permutations:
        print(p)
