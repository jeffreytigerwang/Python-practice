import bisect
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low = matrix[0][0]
        high = matrix[-1][-1]

        while low < high:
            mid = low + (high - low) // 2

            if sum(bisect.bisect_right(matrix[i], mid) for i in range(len(matrix))) < k:
                low = mid + 1
            else:
                high = mid
        return low

sol = Solution()
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(sol.kthSmallest(matrix, k))