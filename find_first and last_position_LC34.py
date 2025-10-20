from typing import List
import sys

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_most_target = findLeft(nums, target)
        right_most_target = findRight(nums, target)

        if left_most_target <= right_most_target:
            return [left_most_target, right_most_target]
        else:
            return [-1, -1]

if __name__ == "__main__":
    # Example: python search_range.py 5 7 7 8 8 10 --target 8
    args = sys.argv[1:]
    target_index = args.index("--target")
    nums = list(map(int, args[:target_index]))
    target = int(args[target_index + 1])
    sol = Solution()
    print(sol.searchRange(nums, target))
