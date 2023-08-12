# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        column = len(board[0])
        # path = []

        def backtracking(r, c, path, word):
            if not word:
                return True

            if r < 0 or c < 0 or r >= row or c >= column or [r, c] in path or board[r][c] != word[0]:
                return False

            path.append([r, c])
            res = backtracking(r + 1, c, path, word[1:]) or backtracking(r - 1, c, path, word[1:]) or backtracking(r, c + 1, path, word[1:]) or backtracking(r, c - 1, path, word[1:])
            path.pop()

            return res

        tempDict = {}

        for i in range(row):
            for j in range(column):
                tempDict[board[i][j]] = 1 + tempDict.get(board[i][j], 0)

        try:
            if tempDict[word[0]] > tempDict[word[-1]]:
                word = word[:: -1]
        except KeyError:
            return False

        for i in range(row):
            for j in range(column):
                if board[i][j] == word[0] and backtracking(i, j, [], word):
                    return True

        return False