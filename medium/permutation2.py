from typing import List



# https://leetcode.com/problems/permutations-ii/submissions/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # same as permuation.
        ans = []
        count = 0

        def rec(updatedNums, temp):
            if (temp not in ans) and (len(temp) == len(nums)):
                ans.append(temp)
                global count
                count = count + 1
                return

            for i in range(len(updatedNums)):
                # temp.append(updatedNums[i])

                rec(updatedNums[:i] + updatedNums[i + 1:], temp + [updatedNums[i]])

        print(ans)
        rec(nums, [])
        print(ans)
        return ans