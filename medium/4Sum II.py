# https://leetcode.com/problems/4sum-ii/
from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # tempDict = dict()
        # length = len(nums1)
        # res = 0
        #
        # for i in range(length):
        #     for j in range(length):
        #         if nums1[i] + nums2[j] not in tempDict:
        #             tempDict[nums1[i] + nums2[j]] = 1
        #         else:
        #             tempDict[nums1[i] + nums2[j]] += 1
        #
        # for k in range(length):
        #     for l in range(length):
        #         if -nums3[k] - nums4[l] not in tempDict:
        #             continue
        #
        #         res += tempDict[-nums3[k] - nums4[l]]
        #
        #
        # # print(tempDict)
        # # print(res)
        # return res

        #   Use defaultdict

        res = 0
        length = len(nums1)
        tempDict = defaultdict(int)

        for i in range(length):
            for j in range(length):
                tempDict[nums1[i] + nums2[j]] += 1

        for i in range(length):
            for j in range(length):
                res += tempDict[-(nums3[i] + nums4[j])]

        return res

def main():
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]

    print(sol.fourSumCount(nums1, nums2, nums3, nums4))


if __name__ == "__main__":
    main()
