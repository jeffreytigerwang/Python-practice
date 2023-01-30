# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height = len(board)
        width = len(board[0])
        usedLetter = []
        tempDictionary = {}

        for i in word:
            tempDictionary[i] = []

        for character in tempDictionary.keys():
            coordsList = [[x, y] for x, li in enumerate(board) for y, val in enumerate(li) if val == character]
            tempDictionary[character].extend(coordsList)

            if not tempDictionary[character]:
                return False

        # print(tempDictionary)

        def recursion(nextCharacterIndex, validCoordinates):
            if nextCharacterIndex >= len(word):
                return True

            # if not validCoordinates:


            for validCoordinate in validCoordinates:
                for nextCharacterCoordinate in tempDictionary[word[nextCharacterIndex]]:
                    # May have more than 1 valid coordinate
                    if validCoordinate == nextCharacterCoordinate and nextCharacterCoordinate not in usedLetter:
                        # print(nextCharacterCoordinate)
                        usedLetter.append(nextCharacterCoordinate)
                        tempCoordiantes = []

                        if self.isValidPos(nextCharacterCoordinate[0] - 1, nextCharacterCoordinate[1], height, width):
                            tempCoordiantes.append([nextCharacterCoordinate[0] - 1, nextCharacterCoordinate[1]])

                        if self.isValidPos(nextCharacterCoordinate[0] + 1, nextCharacterCoordinate[1], height, width):
                            tempCoordiantes.append([nextCharacterCoordinate[0] + 1, nextCharacterCoordinate[1]])

                        if self.isValidPos(nextCharacterCoordinate[0], nextCharacterCoordinate[1] - 1, height, width):
                            tempCoordiantes.append([nextCharacterCoordinate[0], nextCharacterCoordinate[1] - 1])

                        if self.isValidPos(nextCharacterCoordinate[0], nextCharacterCoordinate[1] + 1, height, width):
                            tempCoordiantes.append([nextCharacterCoordinate[0], nextCharacterCoordinate[1] + 1])

                        # return recursion(nextCharacterIndex + 1, tempCoordiantes)
                        if recursion(nextCharacterIndex + 1, tempCoordiantes):
                            return True

                        usedLetter.pop()
                        # print("Next valid duplicate")
                        # print("")

            return False


        for value in tempDictionary[word[0]]:
            # print(value)
            usedLetter.append(value)
            initialValidCoordiantes = []

            if self.isValidPos(value[0] - 1, value[1], height, width):
                initialValidCoordiantes.append([value[0] - 1, value[1]])

            if self.isValidPos(value[0] + 1, value[1], height, width):
                initialValidCoordiantes.append([value[0] + 1, value[1]])

            if self.isValidPos(value[0], value[1] - 1, height, width):
                initialValidCoordiantes.append([value[0], value[1] - 1])

            if self.isValidPos(value[0], value[1] + 1, height, width):
                initialValidCoordiantes.append([value[0], value[1] + 1])

            # print(initialValidCoordiantes)

            if recursion(1, initialValidCoordiantes):
                print(usedLetter)
                return True

            usedLetter.pop()

        return False


    def isValidPos(self, i, j, height, width):
        if (i < 0 or j < 0 or i > height - 1 or j > width - 1):
            return 0
        return 1

        # print(tempDictionary)


def main():
    sol = Solution()
    board = [["A", "A", "A", "A"], ["A", "A", "A", "A"], ["A", "A", "E", "A"]]
    word = "AAAAAAAAB"

    print(sol.exist(board, word))

if __name__ == "__main__":
    main()