# https://leetcode.com/problems/subsets/description/

from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     output = [[]]
    #
    #     for num in nums:
    #         tempList = []
    #
    #         for i in output:
    #             tempList.append(i + [num])
    #
    #         # output = output + [curr + [num] for curr in output]
    #         output = output + tempList
    #
    #     return output

    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backTrack(start, cur_list):
            ans.append(cur_list[:])

            for j in range(start, n):
                cur_list.append(nums[j])
                print(cur_list)
                backTrack(j + 1, cur_list)
                cur_list.pop()

            return

        n = len(nums)
        ans = []

        backTrack(0, [])

        return ans


    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     output = []
    #
    #     for i in range(2 ** n, 2 ** (n + 1)):
    #         # generate bitmask, from 0..00 to 1..11
    #         bitmask = bin(i)[3:]
    #
    #         # append subset corresponding to that bitmask
    #         output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    #         print([nums[j] for j in range(n) if bitmask[j] == '1'])
    #
    #     print(output)

def main():
    nums = [1, 2, 3]

    sol = Solution()
    print(sol.subsets(nums))


if __name__ == "__main__":
    main()

