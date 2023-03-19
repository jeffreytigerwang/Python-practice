# https://leetcode.com/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def NSum(tempNums, N, tempTarget, result, results):
            if N < 2 or N > len(tempNums) or tempNums[0] * N > tempTarget or tempNums[-1] * N < tempTarget:
                return

            if N == 2:
                l = 0
                r = len(tempNums) - 1

                while l < r:
                    s = tempNums[l] + tempNums[r]

                    if s == tempTarget:
                        results.append(result + [tempNums[l], tempNums[r]])

                        l = l + 1   # has to move forward by 1 (r - 1 should also work)

                        while tempNums[l] == tempNums[l - 1] and l < r: # eliminate duplicates
                            l = l + 1
                    elif s < tempTarget:
                        l = l + 1
                    else:
                        r = r - 1

            else:
                for i in range(len(tempNums) - N + 1):
                    if i == 0 or (i > 0 and tempNums[i] != tempNums[i - 1]):
                        NSum(tempNums[i + 1:], N - 1, tempTarget - tempNums[i], result + [tempNums[i]], results)

        nums.sort()
        res = []
        NSum(nums, 4, target, [], res)

        return res


def main():
    sol = Solution()
    nums = [1,2,-2,-1,-1,2,0,2]
    target = 0

    print(sol.fourSum(nums, target))

if __name__ == "__main__":
    main()