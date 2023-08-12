# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # Count number of unique substring of size k
        codeSet = set()

        for i in range(len(s) - k + 1):
            codeSet.add(s[i: i + k])

        return len(codeSet) >= 2 ** k