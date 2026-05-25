class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        profit = 0

        for i in range(len(prices)):

            mini = min(mini, prices[i])

            cost = prices[i] - mini

            profit = max(profit, cost)

        return profit