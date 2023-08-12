from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(nums, path):
            if not nums:
                res.append(path[:])
                return

            for i in range(len(nums)):
                path.append(nums[i])
                backtracking(nums[: i] + nums[i + 1:], path)
                path.pop()

            return

        backtracking(nums, [])

        return res

def main():
    nums = [1, 2, 3]

    solution = Solution()
    print(solution.permute(nums))


if __name__ == '__main__':
    main()