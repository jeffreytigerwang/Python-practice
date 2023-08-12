from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        return res



def main():
    intervals = [[1, 4], [1, 6], [1, 5], [4, 5]]
    solution = Solution()
    print(solution.merge(intervals))


if __name__ == "__main__":
    main()
