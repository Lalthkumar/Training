from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, current_combo):
            if target == 0:
                result.append(current_combo[:])
                return

            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                current_combo.append(candidates[i])
                backtrack(i, target - candidates[i], current_combo)
                current_combo.pop()

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result

if __name__ == "__main__":
    import sys
    import ast

    if len(sys.argv) != 3:
        print("Usage: python combination_sum.py <candidates_list> <target>")
        print("Example: python combination_sum.py \"[2,3,6,7]\" 7")
    else:
        candidates = ast.literal_eval(sys.argv[1])
        target = int(sys.argv[2])
        sol = Solution()
        output = sol.combinationSum(candidates, target)
        print(output)
