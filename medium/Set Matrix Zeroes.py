from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        tempIndex = [[x, y] for x, i in enumerate(matrix) for y, j in enumerate(i) if j == 0]
        print(tempIndex)

        for coordinate in tempIndex:
            matrix[coordinate[0]] = [0 for i in range(len(matrix[coordinate[0]]))]

            for i in range(len(matrix)):
                matrix[i][coordinate[1]] = 0

        print(matrix)


def main():
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]

    sol.setZeroes(matrix)

if __name__ == "__main__":
    main()
