class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s:
            slist = s.split()
            lastWord = slist[-1]

            return len(lastWord)


s = "today is my birthday"
solution = Solution()
print(solution.lengthOfLastWord(s))
