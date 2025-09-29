from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n

if __name__ == "__main__":
    # Example input
    nums = [3, 2, 2, 3]
    val = 3

    sol = Solution()
    new_length = sol.removeElement(nums, val)

    print("New length:", new_length)
    print("Modified array:", nums[:new_length])
