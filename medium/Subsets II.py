from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]

        for i in range(len(nums)):
            # ans.append([nums[i]])

            for j in ans:
                if j + [nums[i]] not in ans:
                    ans = ans + [j + [nums[i]]]
        print(ans)
        return ans


def main():
    nums = [1, 2, 2]

    sol = Solution()
    sol.subsetsWithDup(nums)


if __name__ == "__main__":
    main()
