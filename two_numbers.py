from typing import List
import sys

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for i,num in enumerate(nums):
            if num in complement_dict:
                return [complement_dict[num], i]
            else:
                complement_dict[target-num] = i
        return []

def main():
    if len(sys.argv) < 3:
        print("Usage: python two_numbers.py <target> <num1> <num2> ... <numN>")
        print("Example: python two_numbers.py 9 2 7 11 15")
        sys.exit(1)
    
    try:
        target = int(sys.argv[1])
        nums = [int(x) for x in sys.argv[2:]]
        
        solution = Solution()
        result = solution.twoSum(nums, target)
        
        if result:
            print(f"Indices: {result}")
            print(f"Values: [{nums[result[0]]}, {nums[result[1]]}]")
            print(f"Sum: {nums[result[0]]} + {nums[result[1]]} = {target}")
        else:
            print("No solution found")
            
    except ValueError:
        print("Error: All arguments must be integers")
        sys.exit(1)

if __name__ == "__main__":
    main()
