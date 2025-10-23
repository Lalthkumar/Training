import sys
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > remaining:
                    break
                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return res

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python combination_sum2.py <target> <comma-separated candidates>")
        sys.exit(1)

    target = int(sys.argv[1])
    candidates = list(map(int, sys.argv[2].split(',')))

    sol = Solution()
    result = sol.combinationSum2(candidates, target)
    print("Combinations that sum to", target, "are:")
    for combo in result:
        print(combo)
