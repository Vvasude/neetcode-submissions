class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mini = prices[0]
        profit = 0
        
        for L in range(len(prices)):
            count = prices[L] - mini
            profit = max(count,profit)
            if prices[L]<mini:
                mini = prices[L]
        return profit