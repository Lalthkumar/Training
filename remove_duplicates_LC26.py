from typing import List
import sys

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 1
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

if __name__ == "__main__":
    # Example usage: python remove_duplicates.py "1,1,2,2,3"
    nums = list(map(int, sys.argv[1].split(',')))
    solution = Solution()
    k = solution.removeDuplicates(nums)
    print("Length after removing duplicates:", k)
    print("Modified array:", nums[:k])
