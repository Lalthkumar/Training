class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_so_far = nums[0] 
        current_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max + nums[i])
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far

if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = Solution()
    print("Maximum subarray sum:", sol.maxSubArray(nums))
