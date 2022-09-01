from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def rec(candidates1, currentCandidates, currentSum):
            if currentSum == target:
                res.append(currentCandidates)
                return

            if currentSum > target:
                return

            for i in range(len(candidates1)):
                rec(candidates1[i:], currentCandidates + [candidates1[i]], currentSum + candidates1[i])

        rec(candidates, [], 0)
        return res


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    test = Solution()

    print(test.combinationSum(candidates, target))


if __name__ == "__main__":
    main()
