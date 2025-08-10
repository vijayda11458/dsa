class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float(inf)
        maxVal =0
        for i in range(len(prices)):
            minVal = min(prices[i],minVal)
            profit = prices[i] - minVal
            maxVal = max(profit,maxVal)
        return maxVal