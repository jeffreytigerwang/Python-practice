# https://leetcode.com/problems/hand-of-straights/
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # # Without Heap
        #
        # if len(hand) % groupSize != 0:
        #     return False
        #
        # hand.sort()
        # handDict = {}
        #
        # for i in range(len(hand)):
        #     handDict[hand[i]] = 1 + handDict.get(hand[i], 0)
        #
        # while handDict:
        #     temp = next(iter(handDict.keys()))
        #     handDict[temp] -= 1
        #
        #     if handDict[temp] <= 0:
        #         del handDict[temp]
        #
        #     for i in range(1, groupSize):
        #         if temp + i not in handDict.keys():
        #             return False
        #         else:
        #             handDict[temp + i] -= 1
        #
        #             if handDict[temp + i] <= 0:
        #                 del handDict[temp + i]
        #
        # return True


        # With hashmap
        # 1.
        # if len(hand) % groupSize:
        #     return False
        #
        # count = {}
        #
        # for n in hand:
        #     count[n] = 1 + count.get(n, 0)
        #
        # minH = list(count.keys())
        # heapq.heapify(minH)
        #
        # while minH:
        #     first = minH[0]
        #     count[first] -= 1
        #
        #     if count[first] <= 0:
        #         heapq.heappop(minH)
        #
        #     for i in range(1, groupSize):
        #         if first + i not in count:
        #             return False
        #
        #         count[first + i] -= 1
        #
        #         if count[first + i] <= 0:
        #             if count[first] > 0:  # if i != min/first value --> we have a hole in our dict --> False
        #                 return False
        #
        #             heapq.heappop(minH)
        #
        # return True

        # 2.
        if len(hand) % groupSize:
            return False
    
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True


