# https://leetcode.com/problems/surrounded-regions/
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = len(board)
        column = len(board[0])

        def captureDFS(r, c):
            if r < 0 or c < 0 or r >= row or c >= column or board[r][c] != 'O':
                return

            board[r][c] = 'T'
            captureDFS(r - 1, c)
            captureDFS(r + 1, c)
            captureDFS(r, c - 1)
            captureDFS(r, c + 1)

        for r in range(row):
            captureDFS(r, 0)
            captureDFS(r, column - 1)

        for c in range(column):
            captureDFS(0, c)
            captureDFS(row - 1, c)

        for r in range(row):
            for c in range(column):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(row):
            for c in range(column):
                if board[r][c] == 'T':
                    board[r][c] = 'O'



board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
sol = Solution()
sol.solve(board)