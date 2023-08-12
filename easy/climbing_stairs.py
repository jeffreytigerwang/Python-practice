# https://leetcode.com/problems/climbing-stairs/
class Solution(object):
    def climbStairs(self, n):
        if n <= 3:
            return n

        # res = [0, 1, 2, 3]
        #
        # for i in range(4, n + 1):
        #     res.append(res[i - 1] + res[i - 2])
        #
        # return res[-1]

        # n2 = 2
        # n3 = 3
        #
        # for i in range(4, n + 1):
        #     # temp = n2 + n3
        #     # n2 = n3
        #     # n3 = temp
        #
        #     n2, n3 = n3, n2 + n3
        #
        # return n3

        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]


def main():
    test = 5
    answer = Solution()
    print(answer.climbStairs(5))

if __name__ == '__main__':
    main()