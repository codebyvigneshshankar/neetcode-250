class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_stock = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < curr_stock:
                curr_stock = prices[i]
            else:
                profit = profit + (prices[i] - curr_stock)
                curr_stock = prices[i]
        return profit