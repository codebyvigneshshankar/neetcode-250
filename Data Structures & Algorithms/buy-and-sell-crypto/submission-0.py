class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if stock > prices[i]:
                stock = prices[i]
            else:
                profit = prices[i] - stock
                res = max(profit, res)
        return res