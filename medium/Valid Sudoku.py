class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        boardLength = len(board)
        boardWidth = len(board[0])
        # tempDictionary = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

        temp = []
        for i in range(boardLength):
            temp = []
            for j in range(boardWidth):
                # if board[i][j].isnumeric()
                if board[i][j] != ".":
                    if board[i][j] not in temp:
                        temp.append(board[i][j])
                    else:
                        return False
                        # print("false")

        for i in range(boardWidth):
            temp = []
            for j in range(boardLength):
                # if board[i][j].isnumeric()
                if board[j][i] != ".":
                    if board[j][i] not in temp:
                        temp.append(board[j][i])
                    else:
                        return False
                        # print("false")

        blocks = []
        for i in range(0, boardLength, 3):
            for j in range(0, boardWidth, 3):
                blocks.append(board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3])

        for i in range(len(blocks)):
            temp = []
            for j in range(len(blocks[0])):
                if blocks[i][j] != ".":
                    if blocks[i][j] not in temp:
                        temp.append(blocks[i][j])
                    else:
                        return False
                        # print("false")
        return True
