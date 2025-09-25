from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = sorted(nums1 + nums2)
        length = len(merged_array)
        if length % 2 == 0:
            return (merged_array[length // 2] + merged_array[length // 2 - 1]) / 2
        else:
            return merged_array[length // 2]

if __name__ == "__main__":
    import sys
    import ast

    # Example usage: python median.py "[1, 3]" "[2]"
    nums1 = ast.literal_eval(sys.argv[1])
    nums2 = ast.literal_eval(sys.argv[2])

    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)
    print("Median is:", result)
