# integer array prices on ith day

# single day to buy  neetcoin and a different day in future to sell
# return the maximus profit you can achieve

# [10,1,5,6,7,1]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) < 1):
            return 0

        buying_price = prices[0]
        max_profit = 0
        
        for index in range(1,len(prices)):
            buying_price = min(buying_price, prices[index-1])
            max_profit = max(max_profit, prices[index] - buying_price)
        
        return max_profit
        