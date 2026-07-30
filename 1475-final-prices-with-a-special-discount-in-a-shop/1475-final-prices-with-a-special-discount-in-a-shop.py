class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """ n = len(prices)
        for i in range(n):
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices """

        stack = []

        for i in range(len(prices)-1, -1, -1):
            original = prices[i]

            while stack and stack[-1] > original:
                stack.pop()
            
            if stack:
                prices[i] = original - stack[-1]

            stack.append(original)

        return prices