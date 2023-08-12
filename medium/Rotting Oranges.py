from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COLUMN = len(grid[0])
        time = 0
        fresh = 0
        rottenQ = deque()

        for r in range(ROW):
            for c in range(COLUMN):
                if grid[r][c] == 1:
                    fresh += 1

                if grid[r][c] == 2:
                    rottenQ.append([r, c])

        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # BFS
        while rottenQ and fresh > 0:
            # Use for loop instead of while loop since we want the first n (current length) element and appending
            # more element to the end.
            length = len(rottenQ)
            for i in range(length):
                r, c = rottenQ.popleft()

                for dr, dc in direction:
                    row = r + dr
                    column = c + dc

                    if row in range(ROW) and column in range(COLUMN) and grid[row][column] == 1:
                        grid[row][column] = 2
                        rottenQ.append([row, column])
                        fresh -= 1

            time += 1

        if fresh == 0:
            return time

        return -1