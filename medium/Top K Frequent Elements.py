# https://leetcode.com/problems/top-k-frequent-elements/
import collections
import heapq
from typing import List
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # # with Heap
        # tempDict = collections.Counter(nums)
        #
        # hp = []
        # res = []
        #
        # for key in tempDict.keys():
        #     heappush(hp, [[tempDict[key]], key])
        #
        #     if len(hp) > k:
        #         heappop(hp)
        #
        # while hp:
        #     frequency, num = heappop(hp)
        #     res.append(num)
        #
        # return res

        # with frequency
        # tempDict = collections.Counter(nums)

        # OR
        tempDict = {}
        res = []

        for num in nums:
            tempDict[num] = 1 + tempDict.get(num, 0)

        frequencyMap = [[] for i in range(len(nums) + 1)]


        for num, frequency in tempDict.items():
            frequencyMap[frequency].append(num)

        for i in range(len(frequencyMap) - 1, -1, -1):
            for num in frequencyMap[i]:
                res.append(num)

                if len(res) == k:
                    return res







nums = [3,3,0,1,0]
k = 2

sol = Solution()
sol.topKFrequent(nums, k)