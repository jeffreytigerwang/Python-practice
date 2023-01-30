from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        count = 0
        length = len(intervals)

        # def recursion(tempIntervals : List[List[int]], count : int, length : int):
        #     if count >= length:
        #         return True
        #
        #     for i in range(1, len(intervals)):
        #         if intervals[i][0] <= intervals[i-1][1]:
        #             res.append([intervals[i-1][0], max(intervals[i-1][1], intervals[i][1])])
        #         else:
        #             res.append(intervals[i - 1])
        #
        #             if i == len(intervals) - 1:
        #                 res.append(intervals[i])
        #
        #     recursion(intervals, count + 1, length)



        # recursion(res, count, length)


        for i in intervals:
            if not res:
                res.append(i)
                continue

            if res[-1][1] >= i[0]:
                res[-1] = [res[-1][0], max(res[-1][1], i[1])]
            else:
                res.append(i)



        return res


def main():
    intervals = [[1,4],[1,6],[1,5],[4,5]]
    solution = Solution()
    print(solution.merge(intervals))

if __name__ == "__main__":
    main()