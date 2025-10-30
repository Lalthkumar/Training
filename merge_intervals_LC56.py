from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged

if __name__ == "__main__":
    # Example input
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    result = sol.merge(intervals)
    print("Merged intervals:", result)
