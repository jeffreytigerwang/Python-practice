# https://leetcode.com/problems/detect-squares/description/
from typing import List


class DetectSquares:
    def __init__(self):
        self.points = {}
        self.temp = []

    def add(self, point: List[int]) -> None:
        self.points[(point[0],point[1])] = 1 + self.points.get((point[0],point[1]), 0)
        self.temp.append(point)

    def count(self, point: List[int]) -> int:
        res = 0

        # find squre by checking diagonal points
        for x, y in self.temp:
            if abs(point[0] - x) != abs(point[1] - y) or point[0] == x or point[1] == y:
                continue

            res += self.points.get((x, point[1]), 0) * self.points.get((point[0], y), 0)

        return res

