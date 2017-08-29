class Solution(object):
    def maxProfit(self, prices):
        maxPayout, lowStock = 0, float('inf')

        for i in prices:
            maxPayout = max(maxPayout, i - lowStock)
            lowStock = min(lowStock, i)

        return maxPayout
