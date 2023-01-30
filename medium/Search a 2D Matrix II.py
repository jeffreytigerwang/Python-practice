# https://leetcode.com/problems/search-a-2d-matrix-ii/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # # Starts from bottom left
        # m = len(matrix)
        # n = len(matrix[0])
        #
        # i = m - 1
        # j = 0
        #
        # while i >= 0 and j <= n - 1:
        #     # print(matrix[i][j])
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] < target:
        #         j = j + 1
        #     else:
        #         i = i - 1
        #
        # return False

        # Binary search
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                l = 0
                r = n


                while l < r:
                    mid = l + ((r - l) // 2)

                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid

        return False

def main():
    sol = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5

    print(sol.searchMatrix(matrix, target))

if __name__ == "__main__":
    main()
