class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if (not prices or len(prices)==1):
            return 0

        max_p = 0
        temp = prices[0]
        for i in range(1, len(prices)):
            if temp < prices[i]:
                max_p = max(max_p, prices[i] - temp)
            else:
                temp = prices[i]
        return max_p


prices = []
answer = Solution()
print(answer.maxProfit(prices))
