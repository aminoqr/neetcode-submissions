class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        cheapest = prices[0]
        for price in prices:
            profit = price - cheapest
            if profit > maxprofit:
                maxprofit = profit
            if price < cheapest:
                cheapest = price

        return maxprofit
        