class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            potential_profit = price - min_price
            max_profit = max(max_profit, potential_profit)
            min_price = min(min_price, price)
        
        return max_profit
