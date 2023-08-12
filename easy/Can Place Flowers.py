# https://leetcode.com/problems/can-place-flowers/
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and n == 1:
            return not flowerbed[0]

        if n > (len(flowerbed) // 2 + 1):
            return False

        if len(flowerbed) > 1:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] = 1
                n -= 1

            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] = 1
                n -= 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1

            if n <= 0:
                return True

        return True if n <= 0 else False




