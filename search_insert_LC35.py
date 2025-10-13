from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return l

if __name__ == "__main__":
    import sys
    # Example usage: python script.py 1 3 5 6 --target 5
    nums = list(map(int, sys.argv[1:-2]))
    target = int(sys.argv[-1])
    sol = Solution()
    print(sol.searchInsert(nums, target))
