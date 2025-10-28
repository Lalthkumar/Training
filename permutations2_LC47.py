class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        ans = []
        nums.sort()
        used = [False] * len(nums)

        def backtrack(path: list[int]):
            if len(path) == len(nums):
                ans.append(path.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return ans

if __name__ == "__main__":
    s = Solution()
    result = s.permuteUnique([1, 1, 2])
    print(result)
