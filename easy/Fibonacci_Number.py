class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Solution 1:
        # if n == 0:
        #     return 0
        #
        # if n == 1:
        #     return 1
        #
        # i = 1
        # f0 = 0
        # f1 = 1
        # temp = 0
        # while i < n:
        #     temp = f0 + f1
        #     f0 = f1
        #     f1 = temp
        #     i += 1
        # return temp

        # Solution 2
        # if n <= 1:
        #     return n
        #
        # return self.fib(n - 1) + self.fib(n - 2)

        # Solution 3
        if n <= 1:
            return n

        self.cache = {0: 0, 1: 1}
        return self.memoize(n)

    def memoize(self, N):
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return self.memoize(N)


test = Solution()
print(test.fib(4))
