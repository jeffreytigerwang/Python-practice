class Solution(object):
    # Top down + memorization (dictionary)
    def __init__(self):
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n):
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]



test = 5
answer = Solution()
print(answer.climbStairs(5))
