from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        count = []

        def rec(updatedNums, temp):
            if (temp not in ans) and (len(temp) == len(nums)):
                ans.append(temp)
                count.append('1')
                return

            for i in range(len(updatedNums)):
                # temp.append(updatedNums[i])

                rec(updatedNums[:i] + updatedNums[i+1:], temp + [updatedNums[i]])
        print(ans)
        rec(nums, [])
        print(ans)
        print(count)
        return ans


def main():
    nums = [1, 2, 3]

    solution = Solution()
    print(solution.permute(nums))


if __name__ == '__main__':
    main()